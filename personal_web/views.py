from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from personal_web.models import personal

def home(request):

    gallerys = personal.objects
    return render(request,'home.html',{'gallerys': gallerys})
