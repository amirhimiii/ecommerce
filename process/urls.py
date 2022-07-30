from django.contrib import admin
from django.urls import path, include
from .views import add_to_cart, remove_product_from_cart


urlpatterns = [
    path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>', remove_product_from_cart, name='remove-from-cart'),
]
