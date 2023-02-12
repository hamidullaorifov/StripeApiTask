from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/',views.create_payment_session),
    path('success/',views.success),
]
