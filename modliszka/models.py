from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()


class Card(models.Model):
    products = models.ManyToManyField(Product)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateField(auto_now_add=True)
