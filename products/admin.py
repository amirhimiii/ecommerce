from django.contrib import admin
from .models import Product,Comment



class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['product','title','stars','author',]
    extra = 0 

# class CommentInline(admin.TabularInline):
#     model = Comment
#     fields = ['product','title','stars','author',]
#     # extra






@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    
    inlines = [
        CommentInline,
    ]


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['product','title','stars','author',]

