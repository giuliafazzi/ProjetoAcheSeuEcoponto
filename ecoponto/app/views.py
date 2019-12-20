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

