from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    # return HttpResponse("Hello World")
    return HttpResponse("<h1> Hello world again </h1> ")  # can also sent html element

def home(request):
    return HttpResponse("<h2> This is home. </h2>  ")

def contact_us(request):
    return HttpResponse("<h3> This is cotact. <h3> ")