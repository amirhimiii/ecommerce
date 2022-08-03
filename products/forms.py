from django import forms

from .models import Comment, Product


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("title",'stars')




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description',
        'price','discount_price',
        'active','gender',
        'wear','size',
        'color','image','image2']

    
    
