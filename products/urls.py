from django.urls import path, include
from .views import (ProductListView,
                    ProductDetailView, 
                    CommentCreateView,
                    OrderSummaryView,
                    ProductDeleteView,
                    ProductUpdateView,
                    ProductCreateView,
                    ProductHomeView
                )
                                    

# app_name = 'core'
ProductListView
urlpatterns = [
    path('',ProductHomeView.as_view(),name='product-home'),
    path('product-list/',ProductListView.as_view(),name='product-list'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
    path('comment/<int:product_id>/',CommentCreateView.as_view(),name='comment-create'),
    path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
    path('<int:pk>/delete/',ProductDeleteView.as_view(),name='product-delete'),
    path('<int:pk>/update/',ProductUpdateView.as_view(),name='product-update'),
    path('create/',ProductCreateView.as_view(),name='create')
]
