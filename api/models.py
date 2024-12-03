from django.db import models

class AudioResult(models.Model):
    filename = models.CharField(max_length=255)
    predicted_class = models.CharField(max_length=50)
    confidence = models.FloatField()
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.filename} - {self.predicted_class} ({self.confidence:.2f})"

class ESC50Metadata(models.Model):
    filename = models.CharField(max_length=255, verbose_name="Файл")
    fold = models.IntegerField(verbose_name="Фолд")
    target = models.IntegerField(verbose_name="Індекс класу")
    category = models.CharField(max_length=50, verbose_name="Категорія")
    esc10 = models.BooleanField(verbose_name="ESC-10")
    src_file = models.CharField(max_length=255, blank=True, null=True, verbose_name="Джерело")
    take = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер запису")

    class Meta:
        verbose_name = "Метадані ESC-50"
        verbose_name_plural = "Метадані ESC-50"

    def __str__(self):
        return f"{self.filename} - {self.category}"
