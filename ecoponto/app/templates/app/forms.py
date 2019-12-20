from django import forms
from models import Empresa, Material, Certificado

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [ 'cnpj', 
                   'nome', 
                   'endereco', 
                   'telefone',
                   'email',
                   'compra',
                   'venda',
                   'doacao',
                   'coleta',]


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['material']


class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = ['certificacao']
