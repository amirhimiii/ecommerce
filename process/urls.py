from django.contrib import admin
from django.urls import path, include
from .views import add_to_cart, remove_product_from_cart


urlpatterns = [
    path('<int:pk>/add-to-cart/', add_to_cart, name='add-to-cart'),
    path('<int:pk>/remove-from-cart/', remove_product_from_cart, name='remove-from-cart'),
]
