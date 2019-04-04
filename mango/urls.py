from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('comments/', views.comment_list, name='comment_list'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
    path('products/new', views.product_create, name='product_create'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('products/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
]
