from django.db import models
from asesor.models import Asesor
from login.models import Persona

# Create your models here.
class CatClienteProspecto(models.Model):
    idClienteProspecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class Estatus(models.Model):
    idEstatus = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.nombre,self.descripcion)

class OrigenRecomendacion(models.Model):
    idOrigen = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.nombre,self.descripcion)

class AsesorCliente(models.Model):
    idAsesorCliente = models.AutoField(primary_key=True)
    idCliente = models.OneToOneField(Persona)
    idAsesor = models.OneToOneField(Asesor,on_delete=models.CASCADE)
    idClienteProspecto = models.OneToOneField(CatClienteProspecto)
    idOrigen = models.OneToOneField(OrigenRecomendacion)
    idEstatus = models.OneToOneField(Estatus)
    fechaActualizacion = models.DateField()
    ocupacion = models.CharField(max_length=150, blank=True, null=True)
    dependientes = models.CharField(max_length=150, blank=True, null=True)
    ingresos = models.FloatField(blank=True, null=True)
