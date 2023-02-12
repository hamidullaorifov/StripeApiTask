import stripe
from django.http import JsonResponse
from items.models import Item
from django.conf import settings
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def create_payment_session(request,id):
    item = Item.objects.get(pk=id)
    product = stripe.Product.create(name=item.name)
    price = stripe.Price.create(
    unit_amount=int(item.price*100),
    currency="usd",
    product=product.stripe_id,
    )
    session = stripe.checkout.Session.create(
    line_items=[{
        'price': price,
        'quantity':1
        # 'currency': 'usd',
        
    }],
    # payment_intent_data={
    #     'application_fee_amount': 123,
    #     # 'transfer_data': {
    #     # 'destination': '{{CONNECTED_ACCOUNT_ID}}',
    #     # },
    # },
    mode='payment',
    success_url='http://localhost:8000/buy/success/',
    cancel_url=f'http://localhost:8000/item/{item.pk}',
    )
    return JsonResponse({'session':session})

def success(request):
    return render(request,'payment/success.html')
