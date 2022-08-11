from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render , reverse
from django.views import generic
from .models import Product, Comment, Category
from .forms import CommentForm, ProductForm
from django.shortcuts import get_object_or_404
from process.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model




# class ProductCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Product
#     template_name = "products/product_create.html"
#     form_class = ProductForm
        
#     def form_valid(self, form):
#         new_product = form.save(commit=False)
#         user = self.request.user
#         new_product.user = user
#         new_product.save()
#         return super (ProductCreateView, self).form_valid(form)


class ProductListView(generic.ListView):
    queryset = Product.objects.activated()
    template_name = "products/product_list.html"
    paginate_by =6
    context_object_name = 'products'
    # template_name = "products/product_list.html"

    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        context['category'] = Category.objects.filter(status=True)
        return context



class ProductHomeView(generic.ListView):
    # model = Product
    # context_object_name = 'products'

    queryset = Product.objects.activated()
    template_name = "products/product_home.html"
    



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = 'products'

    # def get_object(self):
    #     slug = self.kwargs.get('slug')
    #     return get_object_or_404(Product.objects.activated() , slug=slug)

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




class OrderSummary(LoginRequiredMixin, generic.View):
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



# class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Product
    
#     template_name = "products/product_update.html"

#     form_class = ProductForm


# def category(request, slug):
#     context = {
#         'category': get_object_or_404(Category, slug=slug, status=True)
#     }
#     return render(request, 'products/category.html', context)

class CategoryList(generic.ListView):
    template_name = 'products/category.html'
    
    def get_queryset(self):
        global category
        slug = self.kwargs.get("slug")
        category = get_object_or_404(Category.objects.activated(), slug=slug)
        return category.products.filter(active=True)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["category"] = category 
            return context

#category
class UserView(generic.ListView):
    template_name = 'products/user_list.html'
    paginate_by = 3
    context_object_name = 'products'
    def get_queryset(self):
        global user
        username = self.kwargs.get("username")
        # user = self.request.user
        user = get_object_or_404(get_user_model(), username=username)
        return user.products.activated()

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["user"] = user 
            return context
        
        




