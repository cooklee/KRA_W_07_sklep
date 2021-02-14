from django import forms
from django.core.exceptions import ValidationError

from modliszka.models import ProductTyp, Product, Topping
from modliszka.validators import check_length, check_if_mail, check_price


class ClientForm(forms.Form):
    first_name = forms.CharField(validators=[check_length])
    last_name = forms.CharField(validators=[check_length])
    email = forms.CharField(validators=[check_if_mail])

    def clean(self):
        clean_data = super().clean()
        if clean_data.get('first_name', '').lower() == 'sławek' and clean_data.get('last_name',
                                                                                   '').lower() == 'bogusławski':
            raise ValidationError("Tego pana nie obsługujemy")
        return clean_data


class ProductForm(forms.Form):
    name = forms.CharField(label='Nazwa')
    price = forms.FloatField(label='Cena', validators=[check_price])
    typ = forms.ModelChoiceField(queryset=ProductTyp.objects.all())


class ProductModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({
            'class': 'niepowtarzalna',
            'min': 0.0,
            'max': 10.0,
            'step': 0.3
        })

    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['typ', 'price']


# <input type='number' value='10' min='0.0' max='10.0' step='0.2' class='special'/>

class PizzaForm(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all(),
                                              widget=forms.CheckboxSelectMultiple
                                              )
