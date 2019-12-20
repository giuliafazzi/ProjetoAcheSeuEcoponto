from django.shortcuts import render
from app.models import Empresa, Material, Certificado

def IndexView(request):
    empresas = Empresa.objects.all()
    materiais = Material.objects.all()
    certificados = Certificado.objects.all()
    
    context = {
        'empresas': empresas,
        'materiais': materiais,
        'certificados': certificados,
    }
    return render(request=request, template_name='app/index.html', context=context)

def EcopontosView(request):
    empresas = Empresa.objects.all()
    materiais = Material.objects.all()
    certificados = Certificado.objects.all()
    
    context = {
        'empresas': empresas,
        'materiais': materiais,
        'certificados': certificados,
    }
    return render(request=request, template_name='app/ecopontos.html', context=context)

def SobreView(request):
    empresas = Empresa.objects.all()
    materiais = Material.objects.all()
    certificados = Certificado.objects.all()
    
    context = {
        'empresas': empresas,
        'materiais': materiais,
        'certificados': certificados,
    }
    return render(request=request, template_name='app/sobre.html', context=context)

def EmpresaView(request):
    empresas = Empresa.objects.all()
    materiais = Material.objects.all()
    certificados = Certificado.objects.all()
    
    context = {
        'empresas': empresas,
        'materiais': materiais,
        'certificados': certificados,
    }
    return render(request=request, template_name='app/empresa.html', context=context)

def DuvidasView(request):
    empresas = Empresa.objects.all()
    materiais = Material.objects.all()
    certificados = Certificado.objects.all()
    
    context = {
        'empresas': empresas,
        'materiais': materiais,
        'certificados': certificados,
    }
    return render(request=request, template_name='app/duvidas.html', context=context)

def ContatoView(request):
    empresas = Empresa.objects.all()
    materiais = Material.objects.all()
    certificados = Certificado.objects.all()
    
    context = {
        'empresas': empresas,
        'materiais': materiais,
        'certificados': certificados,
    }
    return render(request=request, template_name='app/contato.html', context=context)

