from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('register_customer/',views.register_customer,name='register_customer'),
    path('register_retailer/',views.register_retailer,name='register_retailer'),
    path('customers/',views.customers,name='customers'),
    path('retailers/',views.retailers,name='retailers'),
]