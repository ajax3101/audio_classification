import os
import pandas as pd
from api.models import ESC50Metadata

from django.conf import settings
META_PATH = os.path.join(settings.BASE_DIR, 'ESC-50/meta/esc50.csv')

def load_metadata():
    # Загрузка CSV-файла
    if not os.path.exists(META_PATH):
        raise FileNotFoundError(f"Файл {META_PATH} не найден.")
    
    meta_data = pd.read_csv(META_PATH)

    # Загрузка метаданных в базу данных
    for _, row in meta_data.iterrows():
        ESC50Metadata.objects.create(
            filename=row['filename'],
            fold=row['fold'],
            target=row['target'],
            category=row['category'],
            esc10=bool(row['esc10']),
            src_file=row['src_file'],
            take=row['take']
        )
    print("Метаданные успешно загружены в базу данных.")

if __name__ == "__main__":
    load_metadata()
