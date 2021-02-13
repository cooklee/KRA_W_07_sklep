from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from modliszka.forms import ClientForm
from modliszka.models import Client

class IndexView(View):
    def get(self, request):
        return render(request, 'base.html', )

class AddClientView(View):

    def get(self, request):
        form = ClientForm()
        return render(request, 'add_client.html', {'form':form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Client.objects.create(**form.cleaned_data) # Client.objects.create(first_name='adam', last_name="samosia")
        return redirect('index')

