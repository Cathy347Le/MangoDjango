from django.contrib import admin
from .models import Product, Cart

admin.site.register(Cart)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "product_image", "quantity", "price", "cart"]
    list_editable = ["description", "quantity", "price"]

admin.site.register(Product, ProductAdmin)