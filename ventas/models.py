from django.db import models
from productos.models import Servicio
from login.models import Persona
from django.contrib.auth.models import User
# Create your models here.

class PlazoPagos(models.Model):
    idplazo = models.AutoField(primary_key=True)
    nombrePlazo = models.CharField(max_length=10)

class PlanesConcretados(models.Model):
    idPlan = models.AutoField(primary_key=True)
    idAsesor = models.ForeignKey(User)
    idCliente = models.ForeignKey(Persona)
    idServicio = models.ForeignKey(Servicio)
    formaPago = models.ForeignKey(PlazoPagos)
    fechaContratacion = models.DateField()
    numeroPoliza = models.CharField(max_length=10)
    primaNetaAnual = models.FloatField()
    plazoAnos = models.IntegerField()
    valorPlan = models.FloatField()
    observaciones = models.CharField(max_length=300, blank=True, null=True)
