import os
import librosa
import numpy as np
import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.shortcuts import render
from django.conf import settings
from tensorflow.keras.models import load_model
from .models import ESC50Metadata
from .serializers import ESC50MetadataSerializer


from .models import AudioResult

# Пути к модели и метаданным
MODEL_PATH = os.path.join(settings.BASE_DIR, 'model/audio_classification_model.keras')
META_PATH = os.path.join(settings.BASE_DIR, 'ESC-50/meta/esc50.csv')

# Загрузка модели
model = load_model(MODEL_PATH)

# Загрузка классов
def load_classes(meta_path):
    meta_data = pd.read_csv(meta_path)
    classes = meta_data[['target', 'category']].drop_duplicates().sort_values(by='target')
    return classes.set_index('target')['category'].to_dict()

CLASSES = load_classes(META_PATH)

# Функция для извлечения признаков
def extract_features(filepath):
    y, sr = librosa.load(filepath, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

# Класс для обработки загружаемых файлов
class AudioUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        # Получение файла из запроса
        file_obj = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, file_obj.name)

        # Сохранение файла
        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        # Извлечение признаков
        features = extract_features(file_path)
        features = np.expand_dims(features, axis=0)

        # Предсказание модели
        predictions = model.predict(features)
        target_class = np.argmax(predictions)
        confidence = np.max(predictions)
        predicted_class = CLASSES.get(target_class, 'Unknown')

        # Сохранение результата в базу данных
        result = AudioResult(
            filename=file_obj.name,
            predicted_class=predicted_class,
            confidence=confidence
        )
        result.save()

        return Response({
            'predicted_class': predicted_class,
            'confidence': confidence,
            'target_index': target_class
        })

class ESC50MetadataListView(APIView):
    def get(self, request, *args, **kwargs):
        metadata = ESC50Metadata.objects.all()
        serializer = ESC50MetadataSerializer(metadata, many=True)
        return Response(serializer.data) 

def home_view(request):
    return render(request, 'home.html')

def upload_view(request):
    return render(request, 'upload.html')

