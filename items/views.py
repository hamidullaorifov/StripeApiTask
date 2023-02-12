from django.shortcuts import render
from .models import Item

# Create your views here.

def index(request):
    items = Item.objects.all()
    context = {
        'items':items,
    }
    return render(request,'items/index.html',context)

def item_details(request,id):
    item = Item.objects.get(pk=id)
    return render(request,'items/details.html',{'item':item})