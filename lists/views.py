from django.shortcuts import render
from django.http import HttpResponse
home_page = None

def home_page(request):
    return render(request, 'home.html', 
            {'new_item_text': request.POST.get('item_text', ""),})
    # return HttpResponse()
    # return HttpResponse('<html><title>To-Do</title></html>')
# Create your views here.
