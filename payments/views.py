from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic
from .models import CheckoutView
from .forms import CheckoutForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from process.models import Cart , CartItem





class ChekoutView(LoginRequiredMixin,generic.View):
    def get(self , *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form' : form
        }
        return render(self.request,'payments/checkout.html',context)
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        print(self.request.POST)
        try:
            order = Cart.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                address = form.cleaned_data.get('address')
                country = form.cleaned_data.get('country')
                email = form.cleaned_data.get('email')
                phone_number = form.cleaned_data.get('phone_number')
                # save_info = form.cleaned_data.get('save_info')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                cart = form.cleaned_data.get('cart')
                zip_code = form.cleaned_data.get('zip_code')
                checkout = CheckoutView(
                    user = self.request.user,
                    address = address,
                    country = country,
                    # save_info = save_info,
                    first_name = first_name,
                    email=email,
                    last_name = last_name,
                    zip_code=zip_code,
                    phone_number=phone_number,
                    cart=order
                )
                checkout.save()
                Cart.checkout = checkout
                Cart.save()
                #TODO add redirect to payment option
                return redirect('checkout')
            messages.warning(self.request,'Failed checkout')
            return redirect('checkout')
        except ObjectDoesNotExist:
            message.error(self.request,'dont have active order')
            return redirect('order-summary')



