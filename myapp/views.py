from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

def index(request):
    return render(request, 'index.html')  # Render the home.html template

def single(request):
    return render(request, 'single.html')