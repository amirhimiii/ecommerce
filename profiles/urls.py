from django.urls import path
from .views import (
ProductList,  ProductCreateView,
ProductUpdateView , ProductDeleteView, 

)


urlpatterns = [
    path('profile/', ProductList.as_view(), name = 'user-profile'),
    path('product/create/',ProductCreateView.as_view(),name='product-create'),
    path('product/update/<slug:slug>/',ProductUpdateView.as_view(),name='product-update'),
    path('product/delete/<slug:slug>/',ProductDeleteView.as_view(),name='product-delete'),

]
