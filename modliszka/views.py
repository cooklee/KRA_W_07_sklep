from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from modliszka.forms import ClientForm, ProductForm, ProductModelForm, PizzaForm
from modliszka.models import Client, Product, Pizza


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html', )


def przykladowy_widok(request):
    context = {'dd': ' tekst  ze słownika', 'pp': "a to jest ppp"}
    szablon = "ala ma {{dd}} kota <h1>  kot nie lubi ali</h1> <br>{{pp}}"
    for key in context:
        wyrazenie = '{{' + key + '}}'
        if wyrazenie in szablon:
            szablon = szablon.replace(wyrazenie, context[key])
    return HttpResponse(szablon)


class AddClientView(View):

    def get(self, request):
        clients = Client.objects.all()
        form = ClientForm()
        return render(request, 'object_list_view.html', {'form': form, "objects": clients})

    def post(self, request):
        form = ClientForm(request.POST)
        clients = Client.objects.all()
        if form.is_valid():
            Client.objects.create(**form.cleaned_data)  # Client.objects.create(first_name='adam', last_name="samosia")
            return redirect('add_client')
        return render(request, 'object_list_view.html', {'form': form, "objects": clients})



class AddProductView(View):

    def get(self, request):
        form = ProductForm()
        products = Product.objects.all()
        return render(request, 'object_list_view.html', {'form': form, 'objects': products})

    def post(self, request):
        form = ProductForm(
            request.POST)  # jak sie wyświetli ten formularz w HTML dzięki request.POST bedzie wypełniony danymi
        products = Product.objects.all()
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)  # Client.objects.create(first_name='adam', last_name="samosia")
            return redirect('add_product')
        return render(request, 'object_list_view.html', {'form': form, 'objects': products})

class AddProductModelFormView(View):

    def get(self, request):
        form = ProductModelForm()
        products = Product.objects.all()
        return render(request, 'object_list_view.html', {'form': form, 'objects': products})

    def post(self, request):
        form = ProductModelForm(
            request.POST)  # jak sie wyświetli ten formularz w HTML dzięki request.POST bedzie wypełniony danymi
        products = Product.objects.all()
        if form.is_valid():
            p = form.save()
            return redirect('add_product')
        return render(request, 'object_list_view.html', {'form': form, 'objects': products})


class AddPizzaView(View):

    def get(self, request):
        form = PizzaForm()
        products = Pizza.objects.all()
        return render(request, 'object_list_view.html', {'form': form, 'objects': products})

    # def post(self, request):
    #     form = ProductModelForm(
    #         request.POST)  # jak sie wyświetli ten formularz w HTML dzięki request.POST bedzie wypełniony danymi
    #     products = Product.objects.all()
    #     if form.is_valid():
    #         p = form.save()
    #         return redirect('add_product')
    #     return render(request, 'object_list_view.html', {'form': form, 'objects': products})
