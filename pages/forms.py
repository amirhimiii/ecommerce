from django import forms
from .models import Contact
from phonenumber_field.widgets import PhoneNumberPrefixWidget

PAYMENT_CHOICES = [
    ('S','Saman'),
    ('M','Melli')
]



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['name','number','email','text',]

