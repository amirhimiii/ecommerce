from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product

# Create your views here.



# @login_required
# def home(request):
#     return render(request, 'prof/profile_user.html')


class ProductList(LoginRequiredMixin,generic.ListView):
    template_name = 'prof/profile_user.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Product.objects.all()
        else:
            return Product.objects.filter(user=self.request.user)
    
