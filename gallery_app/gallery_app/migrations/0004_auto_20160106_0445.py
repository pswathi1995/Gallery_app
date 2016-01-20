# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import gallery_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0003_auto_20160105_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='video_track',
            field=models.FileField(default='qwe', upload_to=gallery_app.models.getVideo),
        ),
        migrations.AlterField(
            model_name='profile',
            name='audio_track',
            field=models.FileField(upload_to=gallery_app.models.getAudio),
        ),
    ]