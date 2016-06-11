from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('mobile.views',
    url(r'^sfdata/postAudio', 'post_audio_to_speech'),
    url(r'^sfdata/test', 'test'),
)

urlpatterns = format_suffix_patterns(urlpatterns)