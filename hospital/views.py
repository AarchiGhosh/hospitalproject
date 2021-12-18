from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'hospital/404.html',{'header':"Hospital Admission"})
