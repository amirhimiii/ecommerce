from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product





User = get_user_model()

class Cart(models.Model):
    STATUS_PAID = [
        ('NP','Not-Paid'),
        ('P','Paid')
    ]
    
    
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        verbose_name='کاربر سفارش دهنده',
        related_name='orders',
    )
    status = models.CharField(choices= STATUS_PAID,max_length=2 , null=True, blank=True, verbose_name='وضعیت سفارش')
    ordered = models.BooleanField(default=False)
    date_paid = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ و زمان ثبت سفارش')

    def __str__(self):
        return self.user.username
        
    def get_subtotal_price(self):
        return sum(cartitem.get_total_price_url() for cartitem in self.carts.all())


class CartItem(models.Model):
    order = models.ForeignKey(Cart, on_delete=models.CASCADE , related_name = 'carts',blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'output')
    quantity = models.PositiveSmallIntegerField(default=0)
    # slug = models.SlugField()

    def __str__(self):
        return self.product.title

    def get_total_price_url(self):
        return self.quantity * self.product.price





