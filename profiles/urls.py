from django.urls import path
from .views import (
ProductList,  ProductCreateView,
ProductUpdateView ,
ProductDeleteView,
Profile
)


urlpatterns = [
    path('list_product/', ProductList.as_view(), name = 'list_product'),
    path('product/delete/<slug:slug>/',ProductDeleteView.as_view(),name='product-delete'),
    path('product/create/',ProductCreateView.as_view(),name='product-create'),
    path('product/update/<slug:slug>/',ProductUpdateView.as_view(),name='product-update'),
    path('profile/',Profile.as_view(),name='profile'),

]
