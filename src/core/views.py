from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Hello world</h1>")

def healthz(request):
    return HttpResponse("ok")