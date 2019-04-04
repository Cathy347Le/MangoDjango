from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # path('carts/', views.cart_list, name='cart_list'),
    # path('products/<int:pk>', views.product_detail, name='product_detail'),
    # path('carts/<int:pk>', views.cart_detail, name='cart_detail'),
    # path('products/new', views.product_create, name='product_create'),
    # path('carts/new', views.cart_create, name='cart_create'),
    # path('products/<int:pk>/edit', views.product_edit, name='product_edit'),
    # path('carts/<int:pk>/edit', views.cart_edit, name='cart_edit'),
    # path('products/<int:pk>/delete', views.product_delete, name='product_delete'),
    # path('carts/<int:pk>/delete', views.cart_delete, name='cart_delete'),
]
