from django.conf.urls import url
from .views import HomeContent, VideoContent

urlpatterns = [
    url(r'^video/', VideoContent),
    url(r'^', HomeContent)
]
