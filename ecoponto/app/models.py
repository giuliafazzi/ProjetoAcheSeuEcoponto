from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Empresa(models.Model):
    cnpj = models.CharField(max_length=14, null=False, primary_key=True)
    nome = models.CharField(max_length=80, null=False)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    compra = models.BooleanField(null=False, default=False)
    venda = models.BooleanField(null=False, default=False)
    doacao = models.BooleanField(null=False, default=False)
    coleta = models.BooleanField(null=False, default=False)


class Material(models.Model):
    material = models.CharField(max_length=80, null=False)
    empresas = models.ManyToManyField(Empresa, through='Empresa_Material', related_name='materiais')


class Empresa_Material(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    volume = models.IntegerField(validators=[MinValueValidator(1)])


class Certificado(models.Model):
    certificacao = models.CharField(max_length=80, null=False)
    empresas = models.ManyToManyField(Empresa, related_name='certificados')