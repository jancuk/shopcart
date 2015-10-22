from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from decimal import Decimal

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    title  = models.CharField(max_length=255)
    slug    = models.SlugField(blank=True)
    image   = models.ImageField(upload_to='images/%Y/%m/%d', max_length=500,blank=True,null=True)
    price   = models.DecimalField(max_digits=20,decimal_places=2,default=Decimal(0.00))
    def image_tag(self):
        return '<img src="http://localhost:8000%s" width="100" height="100" />' % (self.image.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    brand = models.ForeignKey(Brand)
    category = models.ForeignKey('Category')
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey("self", related_name="children", blank=True, null=True)
    def __str__(self):
        return self.name

class Cart(models.Model):
    cart_id  = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    products    = models.ManyToManyField(Product)
    order_date  = models.DateTimeField(auto_now_add=True)
    customer    = models.ForeignKey(User)
    cart = models.ForeignKey(Cart)
