# arquivo para indexar urls do app

from django.urls import path

# importando arquivo view onde tem a função

from . import views

# indexando páginas

urlpatterns = [
    path('', views.index),
    path('new', views.new)

]
