from django.db import models
from process.models import Cart
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField




PAYMENT_CHOICE = [
    ('Z','ZarinPal'),
    ('S','Shaparak'),
    ('M','Melat')
    ]


class CheckoutView(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='author' )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE , related_name='checkouts') 
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone_number = PhoneNumberField(max_length=14,help_text='e.g:0912 123 4567')
    address = models.CharField( max_length=200, blank=False, null=False)
    country = CountryField(blank_label='(select country)', blank=False, null=False)
    zip_code =models.IntegerField( blank=False, null=False)

    def __str__(self):
        return self.first_name




