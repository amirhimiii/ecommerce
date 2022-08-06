from django.contrib import admin
from .models import Product,Comment
import random


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['product','title','stars','author',]
    extra = 0 
# class CommentInline(admin.TabularInline):
#     model = Comment
#     fields = ['product','title','stars','author',]
#     # extra




num = random.randint(200_000,400_000)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    # prepopulated_fields = {"slug": ("title",)+(num,)}

    inlines = [
        CommentInline,
    ]


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['product','title','stars','author',]

