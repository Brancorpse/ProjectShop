from django.contrib import admin

from .models import Product, Offer

# importando classe produto

# importando classe Offer


# Register your models here.

# aqui, você está dizendo ao Django que vai administrar a página produtos no painel Admin

# Criando admin para manipular cadastro de produtos

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, OfferAdmin)

admin.site.register(Product, ProductAdmin)