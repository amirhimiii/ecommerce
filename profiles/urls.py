from django.urls import path
from .views import ProductList


urlpatterns = [
    path('profile/', ProductList.as_view(), name = 'user_profile')
]
