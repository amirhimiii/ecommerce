from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request,pk):
    product = get_object_or_404(Product, pk=pk)
    order ,created = Cart.objects.get_or_create(user = request.user, is_paid=False)
    cart_item,item_created = CartItem.objects.get_or_create(product=product , order=order)
    cart_qs = Cart.objects.filter(is_paid=False)
    if cart_qs.exists():
        cart = cart_qs[0]
        if Cart.objects.filter(is_paid=False).exists():
            cart_item.quantity += 1
            cart_item.save()
            return redirect('product-list')

        
#agar cart bood (product)ye done be cartitem (quantity) ezafe kon


@login_required
def remove_product_from_cart(request,pk):
    product = get_object_or_404(Product, pk=pk)
    # order = get_object_or_404 (Cart, pk=pk)
    cart_item = CartItem.objects.get(product=product)
    cart_qs = Cart.objects.filter(is_paid=False)
    if cart_qs.exists():
        cart = cart_qs[0]
        if Cart.objects.filter(is_paid=False).exists():
            cart_item.quantity -= 1
            cart_item.save()
            if cart_item.quantity == 0:
                cart_item.delete()
                return redirect('product-list')
        return redirect('product-list')

        
    


