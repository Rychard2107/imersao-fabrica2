from cgitb import html
from http.client import HTTP_VERSION_NOT_SUPPORTED
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(request):
    now = datetime.datetime.now()
    return render(request, 'blog/home.html')

def joia(request):
    return HttpResponse('Da like')
