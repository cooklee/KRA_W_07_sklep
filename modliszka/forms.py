from django import forms


class ClientForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()