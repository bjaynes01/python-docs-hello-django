from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello POWERBI Team - How are you ? ! We are Awesome Right! Right! Right!")
