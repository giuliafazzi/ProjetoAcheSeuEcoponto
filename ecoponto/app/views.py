from django.shortcuts import render, redirect
from app.models import Empresa, Material, Certificado
from app.forms import EmpresaForm, MaterialForm, CertificadoForm

def IndexView(request):
    empresas = Empresa.objects.all()
    materiais = Material.objects.all()
    certificados = Certificado.objects.all()
    empresas_filtro = ''
    
    context = {
        'empresas': empresas,
        'materiais': materiais,
        'certificados': certificados,
        'empresas_filtro': empresas_filtro,
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
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        print(request.POST)

        print('PASSOU')
        
        if form.is_valid():
            print('É VALIDO')
            empresa = form.save()
            
        return redirect('app:admin')

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

def AdminView(request):
    empresas = Empresa.objects.all()
    materiais = Material.objects.all()
    certificados = Certificado.objects.all()
    form = EmpresaForm

    context = {
        'empresas': empresas,
        'materiais': materiais,
        'certificados': certificados,
        'form': form,
    }

    return render(request=request, template_name='app/admin.html', context=context)


def MaterialCreateView(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)

        if form.is_valid():
            material = form.save()
    
    return redirect('app:admin')


def CertificadoCreateView(request):
    if request.method == 'POST':
        form = CertificadoForm(request.POST)

        if form.is_valid():
            certificado = form.save()
    
    return redirect('app:admin')
