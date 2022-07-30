from django.urls import path, include
from .views import ProductListView, ProductDetailView, CommentCreateView
                                    

# app_name = 'core'

urlpatterns = [
    path('',ProductListView.as_view(),name='product-list'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
    path('comment/<int:product_id>/',CommentCreateView.as_view(),name='comment-create')
]