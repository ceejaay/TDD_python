from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item
# home_page = None

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    else:
        new_item_text = ''
    # item = Item()
    # item.text = request.POST.get('item_text', "")
    # item.save()
    items = Item.objects.all()
    return render(request, 'home.html', 
            {'items': items})
    # return HttpResponse()
    # return HttpResponse('<html><title>To-Do</title></html>')
# Create your views here.
