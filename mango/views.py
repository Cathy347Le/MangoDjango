from django.shortcuts import render, redirect
from .models import Product, Cart
# from .forms import ProductForm, CartForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'mango/product_list.html', {'products': products})

def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'mango/cart_list.html', {'carts': carts})

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'mango/product_detail.html', {'product': product})

def cart_detail(request, pk):
    cart = Cart.objects.get(id=pk)
    return render(request, 'mango/cart_detail.html', {'cart': cart})

def addto_cart(request, pk):
    product = Product.objects.get(id=pk)
    product.cart_id = 2
    product.save()
    return render(request, 'mango/product_detail.html', {'product': product})