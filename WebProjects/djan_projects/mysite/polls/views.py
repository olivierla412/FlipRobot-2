
# Create your views here.
from mysite import *
from django.http import HttpResponse


def index(request):
    return HttpResponse('ssd.html')
