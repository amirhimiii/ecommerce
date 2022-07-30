from django.urls import path, include
from .views import *

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about-us/',AboutUsView.as_view(),name='about-us')

]