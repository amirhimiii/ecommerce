from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from accounts.mixins import FieldMixin, FormValidMixin, UserAccessMixin
from django.shortcuts import get_object_or_404

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
    

class ProductCreateView(LoginRequiredMixin, FieldMixin, FormValidMixin ,generic.CreateView):
    model = Product
    template_name = "prof/product_create.html"
        
    # def form_valid(self, form):
    #     new_product = form.save(commit=False)
    #     user = self.request.user
    #     new_product.user = user
    #     new_product.save()
    #     return super (ProductCreateView, self).form_valid(form)


class ProductUpdateView(UserAccessMixin, FieldMixin, FormValidMixin ,generic.UpdateView):
    model = Product
    template_name = "prof/product_create.html"