# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 07:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_gallery', '0007_auto_20160112_0754'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profile',
            new_name='student_info',
        ),
    ]
