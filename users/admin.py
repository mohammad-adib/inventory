from django.contrib import admin
from .models import Customer, Retailer, Manager, MyUser
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Customer)
admin.site.register(Retailer)
admin.site.register(Manager)

