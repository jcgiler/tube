from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings

import os
import youtube_dl
from .models import MetaData
from django.db import IntegrityError

# Create your views here.

def HomeContent(request):
    template = 'home/home.html'
    metadata = MetaData.objects.all().order_by('-pk')
    context = {
        'title': '',
        'ext': '',
        'error': '',
        'display_error': 'none',
        'display_success': 'none',
        'display_spin': 'none',
        'metadata': metadata,
    }

    if request.POST:
        url = request.POST['url']
        option = request.POST['option']
        ydl_opts = {}

        if option == 'mp3':
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192' }]

        # if option == 'mp4':
        #    pass

        ydl_opts['outtmpl'] = os.path.join(settings.MEDIA_ROOT, '%(title)s.' + option)

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                meta = ydl.extract_info(str(url), download=False)

                c = metadata.create(
                    title = meta['title'],
                    extension = option,
                    duration = format(float(meta['duration']) / 60, '.2f'),
                    filesize = format(float(meta['filesize']) / 1048576, '.2f'),
                    download_url = '/media/%s.%s' % (meta['title'], option),
                    video_id = meta['id']
                )

                c.save()

                ydl.download([str(url)]) # Processing video

                context['title'] = meta['title']
                context['ext'] = option
                context['display_success'] = 'block'
                return render(request, template, context)

            except IntegrityError:
                context['error'] = '%s already exist.' % meta['title']
                context['display_error'] = 'block'
                return render(request, template, context)

            except:
                context['error'] = 'URL entered is not valid, try again or enter another.'
                context['display_error'] = 'block'
                return render(request, template, context)

    else:
        return render(request, template, context)
