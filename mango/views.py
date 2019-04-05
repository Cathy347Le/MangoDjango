from django.shortcuts import render, redirect
from .models import Product, Cart
from django.db.models import F
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
    product.cart_id = 1
    product.quantity = F('quantity') + 1
    product.save()
    cart = Cart.objects.get(id=1)
    return render(request, 'mango/cart_detail.html', {'cart': cart})


def add_qty(request, pk):
    product = Product.objects.get(id=pk)
    product.quantity = F('quantity') + 1
    product.save()
    cart = Cart.objects.get(id=1)
    return render(request, 'mango/cart_detail.html', {'cart': cart})


def del_qty(request, pk):
    product = Product.objects.get(id=pk)
    product.quantity = F('quantity') - 1
    product.save()
    cart = Cart.objects.get(id=1)
    return render(request, 'mango/cart_detail.html', {'cart': cart})


def deletefrom_cart(request, pk):
    product = Product.objects.get(id=pk)
    product.cart_id = ""
    product.quantity = 0
    product.save()
    cart = Cart.objects.get(id=1)
    return render(request, 'mango/cart_detail.html', {'cart': cart})
