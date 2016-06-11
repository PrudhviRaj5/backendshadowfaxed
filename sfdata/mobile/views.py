from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# rest_framework
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from mongo_connection import QGMongo
import re
import speech_recognition as sr
# Create your views here. 


def test(request):
    return HttpResponse('Your test is working')


@api_view(['POST'])
def get_audio_to_speech(request):
    print request
    audio_file = request.audio
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
    try:
        print('Google Speech Recognition thinks you said ' + r.recognize_google(audio))
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print('Could not request results from Google Speech Recognition service; {0}'.format(e))