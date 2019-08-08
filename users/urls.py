from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('register/',views.register_customer,name='register'),
    path('managers/',views.managers,name='managers'),
    path('retailers/',views.retailers,name='retailers'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]