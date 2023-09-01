from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    username =models.CharField(max_length=40, blank=False)
    password = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return f"{self.username},{self.password}"

class Customer(models.Model):
    username = models.CharField(max_length=40, blank=False)
    password = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return f"{self.username},{self.password}"

class Category(models.Model) :
    Category_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.Category_name}"

class Product(models.Model):
    product_name = models.CharField(max_length=40, blank=False)
    product_price = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return f"{self.product_name},{self.product_price}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"