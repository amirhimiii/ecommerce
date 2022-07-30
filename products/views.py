from django.shortcuts import render , reverse
from django.views import generic
from .models import Product,Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from process.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist




class ProductListView(generic.ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'products'



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = 'products'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        return context
    


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    # def get_succes_url(self):
    #     return reverse('product-list')


    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])#1 gereftan id
        product =get_object_or_404(Product, id=product_id)#2 badesh dadn id be get_obj
        obj.product = product 

        return super().form_valid(form)




class OrderSummaryView(generic.View):
       def get(self, *args,**kwargs):
        try:
            products = Product.objects.get(active=True)
            order = Cart.objects.get(user= self.request.user , ordered=False)
            cart_item = CartItem.objects.get(order=order, product=products)
            context = {
                'objects':cart_item
            }
            return render(self.request,"products/order-summary.html",context)
        except ObjectDoesNotExist:
            messages.error(self.request,'you do not have active order')
            return redirect('/')




# ProductUpdateView / ProductDeleteView / ProductDeleteView / ContactView
