from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField




PAYMENT_CHOICE = [
    ('Z','ZarinPal'),
    ('S','Shaparak'),
    ('M','Melat')
    ]


class CheckoutView(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    address = models.CharField( max_length=200)
    country = CountryField(blank_label='(select country)')
    zip_code =models.IntegerField()
    # city =  

    def __str__(self):
        return self.first_name














# class OrderSummary(models.Model):

    

#     class Meta:
#         verbose_name = ("ordersummary")
#         verbose_name_plural = ("ordersummarys")

#     def __str__(self):
#         return self.user.username







# class Payment(models.Model):

    

#     class Meta:
#         verbose_name = ("payment")
#         verbose_name_plural = ("payments")

#     def __str__(self):
#         return self.user.username


