from django.urls import path
from stores import views

app_name='stores'

urlpatterns = [
    path('product_list/',views.ProductList.as_view(),name='product_list'),
]
