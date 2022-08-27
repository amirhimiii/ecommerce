from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic
from .models import CheckoutView
from .forms import CheckoutForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from process.models import Cart , CartItem
from django.contrib.auth.decorators import login_required

from azbankgateways import bankfactories, models as bank_models, default_settings as settings
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404



class CheckView(LoginRequiredMixin,generic.View):
    
    def get(self , *args, **kwargs):
        form = CheckoutForm()
        product = CartItem.objects.all()
        cart = Cart.objects.get(user=self.request.user)

        print(cart.get_subtotal_price())
        context = {
            'form' : form,
            'products':product,
            'cart': cart
        }
        return render(self.request,'payments/checkout.html',context)
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        print(self.request.POST)
        try:
            global order
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



from process.models import Cart
from datetime import datetime




@login_required
def go_to_gateway_view(request):
    total = Cart.objects.filter(user=request.user).first().get_subtotal_price()

    # خواندن مبلغ از هر جایی که مد نظر است
    amount = total
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create(bank_models.BankType.ZARINPAL) # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url('/callback-gateway-view')
        bank.set_mobile_number(user_mobile_number)  # اختیاری
    
        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید. 
        bank_record = bank.ready()
        
        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e






from azbankgateways import bankfactories, models as bank_models, default_settings as settings


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return HttpResponse("پرداخت با موفقیت انجام شد.")

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")