from django.urls import path
from carts.views import *

# app_name = 'carts'

urlpatterns= [
    path('cart1',cart,name='cart'),
    path('add_cart/<int:product_id>/',add_cart,name='add_cart'),
]