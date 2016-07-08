from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings

import os
import youtube_dl
import subprocess


# Create your views here.

def HomeContent(request):
    template = 'home/home.html'
    return render(request, template, {})

def VideoContent(request):
    template = 'home/video.html'
    url = request.GET['url']

    ydl_opts = {
            'outtmpl': os.path.join(settings.MEDIA_ROOT, '%(title)s.%(ext)s')
            }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(url)])
        meta = ydl.extract_info(str(url), download=False)

    if request.method == 'GET':
        return render(request, template, { 'title': meta['title'],
            'ext': meta['ext']
            })
