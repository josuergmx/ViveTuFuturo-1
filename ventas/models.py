from django.db import models
from cliente.models import Cliente
from asesor.models import Asesor
from login.models import Persona
from django.contrib.auth.models import User
# Create your models here.

class PlanesConcretados(models.Model):
    idPlan = models.AutoField(primary_key=True)
    idAsesor = models.ForeignKey(User,on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Persona,on_delete=models.CASCADE)
    idServicio = models.ForeignKey(Servicios)
    fechaContratacion = models.TimeField()
    numeroPoliza = models.CharField(max_length=10)
    primaNetaAnual = models.FloatField()
    plazoAnos = models.IntegerField()
    valorPlan = models.FloatField()
    observaciones = models.CharField(max_length=300, blank=True, null=True)
    
