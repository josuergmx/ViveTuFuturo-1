from django.db import models
from cliente.models import AsesorCliente
from asesor.models import Asesor
# Create your models here.


class Estatuscredito(models.Model):
    idestatuscredito = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.nombre,self.descripcion)

class Creditos(models.Model):
    idCredito = models.AutoField(primary_key=True)
    estatusCredito = models.OneToOneField(Estatuscredito)
    idAsesor = models.ForeignKey(Asesor)
    idCliente = models.OneToOneField(AsesorCliente, blank=True, null=True)
