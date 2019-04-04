from django.shortcuts import render, redirect
from .models import Product, Cart
# from .forms import ProductForm, CartForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'mango/product_list.html', {'products': products})