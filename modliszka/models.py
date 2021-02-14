from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProductTyp(models.Model):
    name = models.CharField(max_length=30)

    @mark_safe
    def __str__(self):
        return self.name + "<h1> AA</h1>"

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    typ = models.ForeignKey(ProductTyp, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.typ is not None:
            typ = self.typ.name
        else:
            typ = ""
        return f"{self.name} {self.price} {typ}"


class Card(models.Model):
    products = models.ManyToManyField(Product, through='CarProduct')
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateField(auto_now_add=True)


class CarProduct(models.Model):
    cart = models.ForeignKey(Card, on_delete=models.CASCADE)
    property = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
