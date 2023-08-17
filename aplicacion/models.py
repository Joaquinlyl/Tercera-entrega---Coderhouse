from django.db import models

class seller(models.Model):
    username =models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.username},{self.password}"

class customer(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.username},{self.password}"

class category(models.Model) :
    Category_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.Category_name}"

class product(models.Model):
    product_name = models.CharField(max_length=40)
    product_price = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.product_name},{self.product_price}"