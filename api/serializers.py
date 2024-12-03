from rest_framework import serializers
from .models import AudioResult, ESC50Metadata

class AudioResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioResult
        fields = '__all__'

class ESC50MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESC50Metadata
        fields = '__all__'
        extra_kwargs = {
            'filename': {'label': 'Файл'},
            'fold': {'label': 'Фолд'},
            'target': {'label': 'Індекс класу'},
            'category': {'label': 'Категорія'},
            'esc10': {'label': 'ESC-10'},
            'src_file': {'label': 'Джерело'},
            'take': {'label': 'Номер запису'},
        }
