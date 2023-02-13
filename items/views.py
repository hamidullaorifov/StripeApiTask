from django.shortcuts import render,get_object_or_404
from .models import Item,Order,OrderItem,Discount,Tax
from django.conf import settings
from django.http import JsonResponse
from django.conf import settings
import json,stripe
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
stripe.api_key = settings.STRIPE_SECRET_KEY


STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLISHABLE_KEY
# Create your views here.

def index(request):
    items = Item.objects.all()
    context = {
        'items':items,
        'stripe_key':STRIPE_PUBLIC_KEY,
    }
    return render(request,'items/index.html',context)

def item_details(request,id):
    item = Item.objects.get(pk=id)
    context = {
        'item':item,
        'stripe_key':STRIPE_PUBLIC_KEY,
    }
    return render(request,'items/details.html',context)


def get_currency_course(currency):
    course = {
        'usd':1,
        'rub':0.014
    }
    return course.get(currency,1)


def get_success_url(request):
    url = request.build_absolute_uri(reverse('success'))
    return url
def get_cancel_url(request,id):
    url = request.build_absolute_uri(reverse('item_details',args=[id]))
    return url
@csrf_exempt
def create_checkout_session(request):
    if request.method =='POST':
        body = request.body
        data = json.loads(body)
        orders = data.get('orders',[])
        line_items = []
        
        for order in orders:
            item = get_object_or_404(Item,id=order['id'])
            product = stripe.Product.create(name=item.name)
            price = stripe.Price.create(
                unit_amount=int(float(item.price)*100*get_currency_course(item.currency)),
                currency='usd',
                product=product,
            )
            line_items.append(
                {
                    'price':price,
                    'quantity': order['quantity'],
                }
            )
        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=get_success_url(request),
            cancel_url=get_cancel_url(request,item.pk),
            )
        return JsonResponse({'session':session})
    


def create_payment_session(request,id):
    item = Item.objects.get(pk=id)
    product = stripe.Product.create(name=item.name)
    price = stripe.Price.create(
    unit_amount=int(item.price*100),
    currency=item.currency,
    product=product.stripe_id,
    )
    session = stripe.checkout.Session.create(
    line_items=[{
        'price': price,
        'quantity':1
    }],
    mode='payment',
    success_url=get_success_url(request),
    cancel_url=get_cancel_url(request,item.pk),
    )
    return JsonResponse({'session':session})

def success(request):
    return render(request,'items/success.html')
