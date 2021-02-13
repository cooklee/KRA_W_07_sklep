from django.shortcuts import render

# Create your views here.
from django.views import View
from datetime import datetime

class IndexView(View):
    def get(self, request):
        return render(request, 'base.html', )

class Index2View(View):
    def get(self, request):
        return render(request, 'base.html', {'active':'Ala',})

class Index3View(View):
    def get(self, request):
        return render(request, 'base.html', {'active':'ma Kota',})

class Index4View(View):
    def get(self, request):
        return render(request, 'base.html', {'ptaszek':'sikorka',"date":'ić pan do premiera'} )
