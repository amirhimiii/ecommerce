from django import forms
from .models import CheckoutView
from django_countries.widgets import CountrySelectWidget



class CheckoutForm(forms.ModelForm):
    
    class Meta:
        model = CheckoutView
        fields = ['first_name','last_name','phone_number','email','address','country','zip_code']
        # exclude = ('user',)
        widgets = {
            'country': CountrySelectWidget()
            }
