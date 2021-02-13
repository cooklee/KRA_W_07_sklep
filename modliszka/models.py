from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

class ProductTyp(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    typ = models.ForeignKey(ProductTyp, on_delete=models.CASCADE, null=True)


class Card(models.Model):
    products = models.ManyToManyField(Product)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateField(auto_now_add=True)
