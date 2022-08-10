from django.urls import path, include
from .views import *


app_name = 'pages'

urlpatterns = [
    # path('',HomePageView.as_view(),name='home'),
    path('about-us/',AboutUsView.as_view(),name='about-us'),
    path('contact-us/',ContactView.as_view(),name='contact'),
    path('feedback/',feedback,name='feedback'), 
]