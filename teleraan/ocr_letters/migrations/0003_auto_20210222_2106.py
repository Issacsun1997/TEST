# Generated by Django 2.2 on 2021-02-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_letters', '0002_auto_20210222_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='OCR',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='image_bat',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='ocr_letter',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
