from django.contrib import admin
from django.urls import path, include
from app.views import IndexView, EcopontosView, SobreView, EmpresaView, DuvidasView, ContatoView, AdminView

app_name = 'app'

urlpatterns = [
    path('', IndexView, name='index'),
    path('ecopontos/', EcopontosView, name='ecopontos'),
    path('sobre/', SobreView, name='sobre'),
    path('empresa/', EmpresaView, name='empresa'),
    path('duvidas/', DuvidasView, name='duvidas'),
    path('contato/', ContatoView, name='contato'),
    path('admin-panel/', AdminView, name='admin-panel')
]
