from django.db import models
from cliente.models import Cliente
from asesor.models import Asesor
# Create your models here.

class PlanesConcretados(models.Model):
    idPlan = models.AutoField(primary_key=True)
    idAsesor = models.ForeignKey(Asesor,on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente)
    idServicio = models.ManyToMany(Servicios)
    fechaContratacion = models.TimeField()
    numeroPoliza = models.CharField(max_length=10)
    primaNetaAnual = models.FloatField()
    plazoAnos = models.IntegerField()
    valorPlan = models.FloatField()
    observaciones = models.CharField(max_length=300, blank=True, null=True)
