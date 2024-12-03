# Generated by Django 5.1.3 on 2024-12-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_esc50metadata_esc10_esc50metadata_src_file_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='esc50metadata',
            options={'verbose_name': 'Метадані ESC-50', 'verbose_name_plural': 'Метадані ESC-50'},
        ),
        migrations.AlterField(
            model_name='esc50metadata',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='esc50metadata',
            name='esc10',
            field=models.BooleanField(verbose_name='ESC-10'),
        ),
        migrations.AlterField(
            model_name='esc50metadata',
            name='filename',
            field=models.CharField(max_length=255, verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='esc50metadata',
            name='fold',
            field=models.IntegerField(verbose_name='Фолд'),
        ),
        migrations.AlterField(
            model_name='esc50metadata',
            name='src_file',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Джерело'),
        ),
        migrations.AlterField(
            model_name='esc50metadata',
            name='take',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер запису'),
        ),
        migrations.AlterField(
            model_name='esc50metadata',
            name='target',
            field=models.IntegerField(verbose_name='Індекс класу'),
        ),
    ]
