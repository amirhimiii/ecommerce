from django.contrib import admin
from django.urls import path, include
from .views import add_to_cart, remove_product_from_cart, remove_product


urlpatterns = [
    path('<slug:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
    path('<slug:slug>/remove-from-cart/', remove_product_from_cart, name='remove-from-cart'),
    path('<slug:slug>/remove_product/', remove_product, name='remove-product'),
]
