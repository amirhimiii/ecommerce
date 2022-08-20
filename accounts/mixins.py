from django.http import Http404
from django.shortcuts import get_object_or_404
from products.models import  Product

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['slug','title','description','category','price',
                    'discount_price','image2','image',
                    'wear','size','color','gender','vip'
                    ]
        if request.user.is_superuser:
            self.fields.append('user')
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.active = False
        return super().form_valid(form)


class UserAccessMixin():
    def dispatch(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        if product.user == request.user and product.active == False or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can't see this page.")


