from django.db import models
from asesor.models import Asesor
import login.models as lm
import datetime
from vive import settings
from django.contrib.auth.models import User

# Create your models here

class Estatus(models.Model):
    idEstatus = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class OrigenRecomendacion(models.Model):
    idOrigen = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class AsesorCliente(models.Model):
    idAsesorCliente = models.AutoField(primary_key=True)
    idCliente = models.OneToOneField(lm.Persona,on_delete=models.CASCADE)
    idAsesor = models.ForeignKey(User,on_delete=models.CASCADE)
    clienteProspecto = models.BooleanField()
    Origen = models.ForeignKey(OrigenRecomendacion)
    Estatus = models.ForeignKey(Estatus)
    fechaActualizacion = models.DateField()
    ocupacion = models.CharField(max_length=150, blank=True, null=True)
    dependientes = models.CharField(max_length=150, blank=True, null=True)
    ingresos = models.FloatField(blank=True, null=True)
    link = models.CharField(max_length=300,blank=True, null=True)
    password = models.CharField(max_length=10,blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    activo = models.NullBooleanField()

class RecomendadoCliente(models.Model):
    nombre = models.CharField(max_length=80)
    celular = models.IntegerField()
    estadoCivil = models.ForeignKey(lm.EstadoCivil)
    hijos = models.BooleanField()
