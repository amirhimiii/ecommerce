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
    path('<slug:slug>/',ProductDetailView.as_view(),name='product-detail'),
    path('comment/<slug:product_id>/',CommentCreateView.as_view(),name='comment-create'),
    path('order-summary/',OrderSummaryView.as_view(),name='order-summary'),
    path('<slug:slug>/delete/',ProductDeleteView.as_view(),name='product-delete'),
    path('<slug:slug>/update/',ProductUpdateView.as_view(),name='product-update'),
    path('create/',ProductCreateView.as_view(),name='create')
]
