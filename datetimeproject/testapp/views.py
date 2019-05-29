from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(request):
    d=datetime.datetime.now()
    s='<h1>time is'+str(d)+'</h1>'
    return HttpResponse(s)
