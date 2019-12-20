from django.contrib import admin
from django.urls import path, include
from app.views import IndexView, EcopontosView, SobreView, EmpresaView, DuvidasView 
from app.views import ContatoView, AdminView, MaterialCreateView, CertificadoCreateView

app_name = 'app'

urlpatterns = [
    path('', IndexView, name='index'),
    path('ecopontos/', EcopontosView, name='ecopontos'),
    path('sobre/', SobreView, name='sobre'),
    path('empresa/', EmpresaView, name='empresa'),
    path('duvidas/', DuvidasView, name='duvidas'),
    path('contato/', ContatoView, name='contato'),
    path('admin/', AdminView, name='admin'),
    path('material/', MaterialCreateView, name='admin'),
    path('certificado/', CertificadoCreateView, name='certificado')
]
