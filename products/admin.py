from django.contrib import admin
from .models import Product, Comment, Category
import random
from django.utils.translation import ngettext
from django.contrib import messages






# @admin.action(description='show category from list')
# def make_published(modeladmin, request, queryset):
#     queryset.update(status=True)


# @admin.action(description='hidden category from list')
# def make_published(modeladmin, request, queryset):
#     queryset.update(status=False)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)


    def make_draft(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
            '%d category drafted.',
            '%d  category drafted.',
            updated,
        ) % updated, messages.WARNING)
    
    
    list_display = ('position','title','slug','parent','status',)
    list_filter = ('status',)
    search_fields = ('title','slug')
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published, make_draft]

        



class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['product','title','stars','author','active']
    extra = 0 


# class CommentInline(admin.TabularInline):
#     model = Comment
#     fields = ['product','title','stars','author',]
#     # extra



# @admin.action(description='show product on website')
# def make_active_product(modeladmin, request, queryset):
#     queryset.update(active=True)

# @admin.action(description='hidden product on website')
# def make_deactive_product(modeladmin, request, queryset):
#     queryset.update(active=False)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def make_active_product(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)


    def make_deactive_product(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, ngettext(
            '%d story was  deactive.',
            '%d stories were deactive.',
            updated,
        ) % updated, messages.WARNING)
    

    list_display = ['title','image_on_admin_pannel','slug','category_to_str','gender','color','active']
    actions = [make_deactive_product,make_active_product]
    inlines = [CommentInline,]
    list_filter = ('title','color','gender','size')
    search_fields = ('title','slug','category_to_str')


    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    category_to_str.short_description='دسته بندی'


