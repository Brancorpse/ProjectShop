from django.http import HttpResponse

from django.shortcuts import render

# importando classe produto

from .models import Product

# Primeira classe importada acima vai retornar objeto para a página web, pela função

# Create your views here.

# criando função para visualização do app web

# parametro vai descobrir informações sobre o cliente

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


# nova função para enviar mensagem para nova página

def new(request):
    return HttpResponse('New Products')





