"""sklep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from modliszka import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name='index'),
    path("ala/", views.przykladowy_widok, name='ala'),
    path("addClient/", views.AddClientView.as_view(), name='add_client'),
    path("addProduct/", views.AddProductModelFormView.as_view(), name='add_product'),
    path("addPizza/", views.AddPizzaView.as_view(), name='add_pizza'),
    path("contactForm/", views.ContactView.as_view(), name='contactForm'),
]
