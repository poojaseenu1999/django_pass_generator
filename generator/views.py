from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('hello! pooja seenu!')
def eggs(request):
    return HttpResponse('eggs are so tasty!!')
