from django import forms
from modliszka.models import ProductTyp


class ClientForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()


class ProductForm(forms.Form):
    name = forms.CharField(label='Nazwa')
    price = forms.FloatField(label='Cena')
    typ = forms.ModelChoiceField(queryset=ProductTyp.objects.all())