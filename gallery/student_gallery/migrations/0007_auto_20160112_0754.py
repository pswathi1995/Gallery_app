# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 07:54
from __future__ import unicode_literals

from django.db import migrations, models
import student_gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('student_gallery', '0006_remove_profile_studentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='video_track',
            field=models.FileField(default='', upload_to=student_gallery.models.getVideo),
        ),
    ]
