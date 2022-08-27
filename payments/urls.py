from django.urls import path
from .views import CheckView 



urlpatterns = [
    path('checkout/',CheckView.as_view(),name='checkout'),
]

