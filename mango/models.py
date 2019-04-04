from django.db import models

class Cart(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=750)
    product_image = models.CharField(max_length=500)
    price = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
            return self.name



