from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from subby.models.image import SubletImage
# Create your views here.

def index(req):
    images = SubletImage.objects.all()
    return render(req, 'application/base.html', {'images' : images})
