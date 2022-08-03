from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = PhoneNumberField(max_length=14,help_text='e.g:0912 123 4567')
    email = models.EmailField(max_length=254)
    text = models.TextField()

    def __str__(self):
        return self.name