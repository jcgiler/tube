# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170731_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='video_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
