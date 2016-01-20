# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import gallery_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0002_auto_20151224_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='audio_track',
            field=models.FileField(default='qwe', upload_to=gallery_app.models.getAudio),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(upload_to=gallery_app.models.getImage),
        ),
    ]