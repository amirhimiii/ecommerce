from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render , reverse
from django.views import generic
from .models import Product,Comment
from .forms import CommentForm, ProductForm
from django.shortcuts import get_object_or_404
from process.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist



class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    template_name = "products/product_create.html"
    form_class = ProductForm
        
    def form_valid(self, form):
        new_product = form.save(commit=False)
        user = self.request.user
        new_product.user = user
        new_product.save()
        return super (ProductCreateView, self).form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    paginate_by =4
    template_name = "products/product_list.html"
    context_object_name = 'products'



class ProductHomeView(generic.ListView):
    model = Product
    template_name = "products/product_home.html"
    context_object_name = 'products'



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = 'products'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        return context
    


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    # template_name = "products/comment_form.html"



    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])#1 gereftan id
        product =get_object_or_404(Product, id=product_id)#2 badesh dadn id be get_obj
        obj.product = product 

        return super().form_valid(form)




class OrderSummaryView(LoginRequiredMixin, generic.View):
    def get(self, *args, **kwargs):
        try:
            order = Cart.objects.get(user=self.request.user, is_paid=False)
            context = {
                'order': order
            }
            return render(self.request, "products/order-summary.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, 'you do not have active order')
            return redirect('/')



class ProductDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy('product-list')
    context_object_name = 'products'


    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user



class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    
    template_name = "products/product_update.html"

    form_class = ProductForm




