import os
import librosa
import numpy as np
import pandas as pd

DATASET_PATH = '../ESC-50/audio'
META_PATH = '../ESC-50/meta/esc50.csv'
OUTPUT_FEATURES = 'features.npz'

meta = pd.read_csv(META_PATH)

def extract_features(file_name):
    audio, sr = librosa.load(file_name, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def preprocess():
    features, labels = [], []
    for i, row in meta.iterrows():
        file_path = os.path.join(DATASET_PATH, row['filename'])
        try:
            features.append(extract_features(file_path))
            labels.append(row['target'])
        except Exception as e:
            print(f"Ошибка обработки файла {file_path}: {e}")

    # Сохранение результатов
    np.savez(OUTPUT_FEATURES, features=np.array(features), labels=np.array(labels))
    print(f"Данные сохранены в {OUTPUT_FEATURES}")

if __name__ == "__main__":
    preprocess()
