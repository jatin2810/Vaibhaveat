from django.shortcuts import render,HttpResponse
from landing import views
# Create your views here.

def landing(request):
    return render(request,"landing.html")

def index(request):
    return render(request,"index.html")
