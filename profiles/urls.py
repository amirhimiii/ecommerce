from django.urls import path
from .views import ProductList,  ProductCreateView 


urlpatterns = [
    path('profile/', ProductList.as_view(), name = 'user-profile'),
    path('product/create/',ProductCreateView.as_view(),name='prodcut-create'),
    # path('product/update/',ProductCreateView.as_view(),name='produt-update'),


]
