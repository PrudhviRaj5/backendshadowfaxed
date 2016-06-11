from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .forms import UploadFileForm
# rest_framework
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from mongo_connection import QGMongo
import re
import speech_recognition as sr
from subprocess import call
import os
# Create your views here. 


def test(request):
    return HttpResponse('Your test is working')


@api_view(['POST'])
def post_audio_to_speech(request):
    form = UploadFileForm(request.POST, request.FILES)
    f = request.FILES['testing']
    try:
        with open('mobile/media-chunk/sample.3gp', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    except(e):
        return Response({'status': 'fail', 'msg': str(e)}, status=404)
    # convert 3gp to wav api
    try:
        call(['bash', './mobile/test.sh'])
        AUDIO_FILE = './mobile/media-chunk/sample.wav'
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
        try:
            print('Google Speech Recognition thinks you said ' + r.recognize_google(audio))
        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')
        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition service; {0}'.format(e))

        return Response({'status': 'success'}, status=200)
    except(e):
        return Response({'status': 'fail', 'msg': str(e)}, status=404)

