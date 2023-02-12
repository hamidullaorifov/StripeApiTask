from django.shortcuts import render
from .models import Item
from django.conf import settings

STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLISHABLE_KEY
# Create your views here.

def index(request):
    items = Item.objects.all()
    context = {
        'items':items,
    }

    return render(request,'items/index.html',context)

def item_details(request,id):
    item = Item.objects.get(pk=id)
    context = {
        'item':item,
        'stripe_key':STRIPE_PUBLIC_KEY,
    }
    return render(request,'items/details.html',context)