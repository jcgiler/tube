# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_metadata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='video_id',
            field=models.CharField(default='1234', max_length=255),
        ),
    ]