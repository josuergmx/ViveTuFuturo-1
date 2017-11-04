from django.db import models
from login.models import Persona
from cliente.models import AsesorCliente
# Create your models here.

class CatEstatuscita(models.Model):
    idEstatus = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return (self.nombre)

class CatTipocita(models.Model):
    idTipoCita = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return (self.nombre)


class Cita(models.Model):
    idCita = models.BigIntegerField(primary_key=True)
    idAsesorCliente = models.ForeignKey(AsesorCliente,on_delete=models.CASCADE)
    idTipoCita = models.OneToOneField(CatTipocita)
    idEstatus = models.OneToOneField(CatEstatuscita)
    fecha = models.DateTimeField()
    direccionCita = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
