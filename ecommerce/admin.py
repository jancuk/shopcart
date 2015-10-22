from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Cart)
