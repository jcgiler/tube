from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings

import os
import youtube_dl
import subprocess


# Create your views here.

def HomeContent(request):
    template = 'home/home.html'

    if request.GET:
        url = request.GET['url']
        option = request.GET['option']

        ydl_opts = {
                'outtmpl': os.path.join(settings.MEDIA_ROOT, '%(title)s.%(ext)s')
                }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([str(url)])
                meta = ydl.extract_info(str(url), download=False)
                if request.method == 'GET':
                    return render(request, template, {
                            'title': meta['title'],
                            'ext': meta['ext'],
                            'display_success': 'block',
                            'display_spin': 'none',
                        })
            except:
                return render(request, template, {
                        'error': 'Url incorrecta, prueba de nuevo con otra...',
                        'display_error': 'block',
                        'display_spin': 'none',
                    })
    else:
        return render(request, template, {})
