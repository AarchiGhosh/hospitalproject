from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'hospital/base.html',{'year':"2022"})