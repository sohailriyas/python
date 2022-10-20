from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('<h1> Hello django </h1>')
# Create your views here.
