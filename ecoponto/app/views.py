from django.shortcuts import render
from app.models import Empresa, Material, Certificado

def IndexView(request):
    empresas = Empresa.objects.all()
    context = {'empresas': empresas}
    return render(request=request, template_name='app/index.html', context=context)

