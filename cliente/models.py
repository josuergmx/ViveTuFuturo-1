from django.db import models
from login.models import Persona
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
    idCliente = models.OneToOneField(lm.Persona)
    idAsesor = models.ForeignKey(User)
    clienteProspecto = models.BooleanField()
    Origen = models.ForeignKey(OrigenRecomendacion,blank=True, null=True)
    Estatus = models.ForeignKey(Estatus,blank=True, null=True) #Para saber en que estado me quede, si en sesiòn 1, sesiòn 2, etc...
    estatusCita = models.CharField(max_length=2,blank=True, null=True) #Para saber en que estado se quedo la ultima cita, si fue cancelada, si esta en espera de confirmaciòn o si ya es un hecho.
    fechaActualizacion = models.DateField()
    fecha = models.DateTimeField(blank=True, null=True)
    ocupacion = models.CharField(max_length=150, blank=True, null=True)
    dependientes = models.CharField(max_length=150, blank=True, null=True)
    ingresos = models.FloatField(blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    activo = models.NullBooleanField()
    def __str__(self):
        return(self.idCliente.user.username +" "+self.idAsesor.username)


class RecomendadoCliente(models.Model):
    nombre = models.CharField(max_length=80)
    vivienda = models.CharField(max_length=80,blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    estadoCivil = models.ForeignKey(lm.EstadoCivil,blank=True, null=True)
    hijos = models.BooleanField()
    asesor = models.ForeignKey(Persona,blank=True, null=True)
    activo = models.NullBooleanField()
