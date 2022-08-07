from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save , post_save
from .utils import slugify_instance_title
from django.utils.translation import gettext_lazy as _
import random



class Category(models.Model):
    title = models.CharField(max_length=100 ,verbose_name=_('name'))
    slug = models.SlugField(unique = True, blank=True , null=True)
    position = models.IntegerField(verbose_name = _('position'))
    status = models.BooleanField(default= True, verbose_name=_('status'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = [ 'position' ]

    def __str__(self):
        return self.title
    



class Product(models.Model):

    PRODUCT_GENDER = [
        ('W',_('Womans')),
        ('M',_('Mans'))
    ]

    PRODUCT_CHOICES = [
        ('T',_('T-shirt')),
        ('J',_('Jeens')),
        ('S',_('Shoes'))
        ]

    PRODUCT_SIZE = [
            ('L',_('Large')),
            ('S',_('Small')),
            ('M',_('Medium'))
        ]

    PRODUCT_COLOR = [
        ('B',_('Black')),
        ('W',_('White')),
        ('G',_('green')),
        ('R',_('Red')),
        ('BL',_('Blue')),
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100 ,verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'))
    category = models.ManyToManyField(Category, verbose_name=_("category"), related_name="products")

    price = models.PositiveIntegerField(verbose_name=_('price'))
    discount_price = models.IntegerField(blank=True,null=True, verbose_name=_('discount price'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    
    image2 = models.ImageField(upload_to='image/',blank=True,null=True,default = 'image/117515975.jpg', verbose_name=_('image2'))
    image = models.ImageField(upload_to='image/',blank=False,null=False,default = None, verbose_name=_('image'))
    wear = models.CharField(choices=PRODUCT_CHOICES,max_length=1, verbose_name=_('product choice'))
    size = models.CharField(choices=PRODUCT_SIZE, max_length=1, verbose_name=_('size'))
    color = models.CharField(choices=PRODUCT_COLOR, max_length=2, verbose_name=_('color'))
    gender = models.CharField(choices=PRODUCT_GENDER , max_length=1, verbose_name=_('gender'))
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    slug = models.SlugField(unique = True, blank=True , null=True)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def category_published(self):
        return self.category.filter(status= True)


    



#slug
def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Product)


def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance_title(instance, save=True)
        # instance.slug =self.slug
        # instance.save()

post_save.connect(article_post_save, sender=Product)







class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)



class Comment(models.Model):
    COMMENT_STAR = [
        ('1',_('VeryBad')),
        ('2',_('Bad')),
        ('3',_('Good')),
        ('4',_('VeryGood')),
        ('5',_('Perfect')),
    ]
    
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = 'comments',)
    product =models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'comments',)
    
    title = models.TextField(verbose_name= _('comment text'))
    stars = models.CharField(max_length=50, choices=COMMENT_STAR, verbose_name= _('your stars'))
    
    datetime_created = models.DateField(auto_now_add=True)
    datetime_modified = models.DateField(auto_now=True)
    active = models.BooleanField(default = True)


    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.product.slug])






