from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('item/<int:id>/',views.item_details,name='item_details'),
    path('order/',views.create_checkout_session),
    path('buy/<int:id>/',views.create_payment_session),
    path('success/',views.success,name='success'),
]
