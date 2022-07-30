from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product







class Cart(models.Model):
    user = models.ForeignKey(get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='کاربر سفارش دهنده',
        related_name='orders',
    )
    order_no = models.IntegerField(unique=True, null=True, blank=True, verbose_name='شماره سفارش')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده/ نشده')
    status = models.CharField(max_length=200, null=True, blank=True, verbose_name='وضعیت سفارش')
    ordered = models.BooleanField(default=False)
    date_paid = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ و زمان ثبت سفارش')

    def __str__(self):
        return self.user.username
        



class CartItem(models.Model):
    order = models.ForeignKey(Cart, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f' {self.product.title} - {self.order}'











class Checkout(models.Model):  # dakhel app jadid bzarm pardakhtaro
    pass


class Payment(models.Model): # dakhel app jadid bzarm pardakhtaro
    pass