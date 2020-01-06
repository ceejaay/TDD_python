from django.shortcuts import render
from django.http import HttpResponse
home_page = None

def home_page(request):
    # return HttpResponse()
    return HttpResponse('<html><title>To-Do</title></html>')
# Create your views here.
