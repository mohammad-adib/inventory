from django.contrib import admin
from .models import Retailer,Customer 
from stores.models import Store
# Register your models here.



# class RetailerInline(admin.StackedInline):
    
#     model = Retailer
#     fk_name='store'
#     # extra=1

# class StoreAdmin(admin.ModelAdmin):
#     inlines = [RetailerInline,]

admin.site.register(Retailer)
# admin.site.register(Retailer,StoreAdmin)
admin.site.register(Customer)

# admin.site.register(Retailer)
