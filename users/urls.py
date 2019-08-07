from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('register_customer/',views.register_customer,name='register_customer'),
    path('customers/',views.customers,name='customers'),
    path('retailers/',views.retailers,name='retailers'),
    path('login/',views.login,name='login'),
]