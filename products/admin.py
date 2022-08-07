from django.contrib import admin
from .models import Product, Comment, Category
import random



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status',)
    list_filter = ('status',)
    search_fields = ('title','slug')
    prepopulated_fields = {"slug": ("title",)}
        




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
    list_display = ['title','slug','category_to_str']
    inlines = [
        CommentInline,
    ]

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    category_to_str.short_description='دسته بندی'


