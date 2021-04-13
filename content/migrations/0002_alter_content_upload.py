# Generated by Django 3.2 on 2021-04-07 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='upload',
            field=models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'MP4'])]),
        ),
    ]