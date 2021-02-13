from django import forms
from django.core.exceptions import ValidationError

from modliszka.models import ProductTyp

def check_price(value):
    if float(value) < 0:
        raise ValidationError("Cena nie może być mniejsza niż zero")


class ClientForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()


class ProductForm(forms.Form):
    name = forms.CharField(label='Nazwa')
    price = forms.FloatField(label='Cena', validators=[check_price])
    typ = forms.ModelChoiceField(queryset=ProductTyp.objects.all())