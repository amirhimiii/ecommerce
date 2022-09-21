from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ['product','order','quantity']
#     list_filter = ('product','order')




class CartInline(admin.StackedInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','status','ordered','date_paid']
    list_filter = ('user','status','ordered','date_paid')
    inlines = [CartInline,]

admin.site.register(CartItem)