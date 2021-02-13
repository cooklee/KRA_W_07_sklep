from django import forms
from django.core.exceptions import ValidationError

from modliszka.models import ProductTyp

def check_price(value):
    if value < 0:
        raise ValidationError("Cena nie może być mniejsza niż zero")

def check_length(value):
    if len(value) < 3:
        raise ValidationError("za krótkie")

def check_if_mail(value):
    if '@' not in value:
        raise ValidationError("a gdzie małpa Cholero!!!")



class ClientForm(forms.Form):
    first_name = forms.CharField(validators=[check_length])
    last_name = forms.CharField(validators=[check_length])
    email = forms.CharField(validators=[check_if_mail])

    def clean(self):
        clean_data = super().clean()
        if clean_data.get('first_name', '').lower() == 'sławek' and clean_data.get('last_name', '').lower() == 'bogusławski':
            raise ValidationError("Tego pana nie obsługujemy")
        return clean_data


class ProductForm(forms.Form):
    name = forms.CharField(label='Nazwa')
    price = forms.FloatField(label='Cena', validators=[check_price])
    typ = forms.ModelChoiceField(queryset=ProductTyp.objects.all())