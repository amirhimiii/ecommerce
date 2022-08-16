from django.urls import path, include
from .views import(ProductListView, 
ProductDetailView,
 CommentCreateView,
 OrderSummary,
 ProductHomeView,
 CategoryList,
 UserView,
ProductPreview
)
                         



urlpatterns = [
    path('',ProductHomeView.as_view(),name='product-home'),
    path('category/<slug:slug>/' , CategoryList.as_view(), name='category'),
    
    path('preview/<slug:slug>/',ProductPreview.as_view(),name='product-preview'),
    path('order-summary/',OrderSummary.as_view(),name='order-summary'),
    
    path('product-list/',ProductListView.as_view(),name='product-list'),
    path('user/<slug:username>/',UserView.as_view(),name='user'),
    
    path('<slug:slug>/',ProductDetailView.as_view(),name='product-detail'),
    path('comment/<slug:product_id>/',CommentCreateView.as_view(),name='comment-create'),

]

