from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save , post_save
from .utils import slugify_instance_title
import random


PRODUCT_GENDER = [
    ('W','Womans'),
    ('M','Mans')
]

PRODUCT_CHOICES = [
    ('T','T-shirt'),
    ('J','Jeens'),
    ('S','Shoes')
    ]

PRODUCT_SIZE = [
        ('L','Large'),
        ('S','Small'),
        ('M','Medium')
    ]

PRODUCT_COLOR = [
    ('B','Black'),
    ('W','White'),
    ('G','green'),
    ('R','Red'),
    ('BL','Blue'),
]


class Product(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    price = models.PositiveIntegerField()
    discount_price = models.IntegerField(blank=True,null=True)
    active = models.BooleanField(default=True)
    
    image2 = models.ImageField(upload_to='image/',blank=True,null=True,default = 'image/117515975.jpg')
    image = models.ImageField(upload_to='image/',blank=False,null=False,default = None)
    wear = models.CharField(choices=PRODUCT_CHOICES,max_length=1)
    size = models.CharField(choices=PRODUCT_SIZE, max_length=1)
    color = models.CharField(choices=PRODUCT_COLOR, max_length=2)
    gender = models.CharField(choices=PRODUCT_GENDER , max_length=1)
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    slug = models.SlugField(unique = True, blank=True , null=True)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.pk])


    

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
        ('1','VeryBad'),
        ('2','Bad'),
        ('3','Good'),
        ('4','VeryGood'),
        ('5','Perfect'),
    ]
    
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = 'comments',)
    product =models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'comments',)
    
    title = models.TextField(verbose_name='body')
    stars = models.CharField(max_length=50, choices=COMMENT_STAR)
    
    datetime_created = models.DateField(auto_now_add=True)
    datetime_modified = models.DateField(auto_now=True)
    active = models.BooleanField(default = True)


    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.product.id])






