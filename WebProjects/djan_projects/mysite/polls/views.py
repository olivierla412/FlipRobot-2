
# Create your views here.
from django.shortcuts import render
from mysite import *
from django.http import HttpResponse, request
def index(request):
    return HttpResponse('ssd.html')
    


