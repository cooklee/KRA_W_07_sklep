from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from modliszka.validators import check_price, check_length


class Client(models.Model):
    first_name = models.CharField(max_length=128, validators=[check_length])
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProductTyp(models.Model):
    name = models.CharField(max_length=30)

    @mark_safe
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa')
    description = models.CharField(max_length=256, verbose_name="Opis", default='')
    price = models.FloatField(verbose_name='Cena', validators=[check_price])
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

SIZES = (
    (1, 'small'),
    (2, 'normal'),
    (3, 'large'),
)

class Topping(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=128)
    size = models.IntegerField(choices=SIZES)
    toppings = models.ManyToManyField(Topping)
    price = models.FloatField()




