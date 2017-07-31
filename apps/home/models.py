from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MetaData(models.Model):

    title = models.CharField(max_length=255)
    extension = models.CharField(max_length=3)
    duration = models.CharField(max_length=10)
    filesize = models.CharField(max_length=10)
    download_url = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return  self.title
