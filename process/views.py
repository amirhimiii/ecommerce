from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

rand = random.randint(100_000,500_000)


@login_required
def add_to_cart(request,slug):
    product = get_object_or_404(Product, slug=slug)
    # order,create = Cart.objects.get_or_create(user=request.user,status='NP', ordered=True, date_paid=timezone.now())
    # order = Cart.objects.filter(user=request.user).first()
    try:
        order = Cart.objects.get(user=request.user, ordered=True)
    except ObjectDoesNotExist:
        order = Cart.objects.create(user=request.user, status='NP', ordered=True, date_paid=timezone.now())
    
    cart_item_created, cart_item  = CartItem.objects.get_or_create(product=product , order=order )
    if cart_item_created:
        cart_item_created.quantity += 1
        cart_item_created.save()
        messages.success(request,f'<< {product.title} >> add to cart')
        return redirect('order-summary')
    messages.success(request,f'{product.title} add to cart')
    return redirect('product-list')

#agar cart bood (product)ye done be cartitem (quantity) ezafe kon


@login_required
def remove_product_from_cart(request,slug):
    cart_item= get_object_or_404(CartItem, order__user=request.user, product__slug=slug)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        messages.warning(request,f'one order of << {cart_item.product.title} >> deleted ')
        return redirect('order-summary')
    else:
        messages.warning(request,f'<< {cart_item.product.title} >>delete from cart')
        cart_item.delete()
        return redirect('product-list')



def remove_product(request, slug):
    cart_item= get_object_or_404(CartItem, order__user=request.user, product__slug=slug)
    messages.warning(request,f'<< {cart_item.product.title} >>delete from cart')
    cart_item.delete()
    return redirect('order-summary')

    




    


