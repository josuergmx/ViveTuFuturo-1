from django.db import models
from login.models import Persona
from django.contrib.auth.models import User
from aseguradoras.models import Servicios
# Create your models here.

class ReporteActividad(models.Model):
    idReporte = models.AutoField(primary_key=True)
    idAsesor = models.ForeignKey(User,on_delete=models.CASCADE)
    fechaReporte = models.DateField()
    recomendadosObtenidos = models.IntegerField()
    recomendadosContactados = models.IntegerField()
    llamadasRealizadas = models.IntegerField()
    citasObtenidas = models.IntegerField()
    citasTotales = models.IntegerField()
    citasNuevas = models.IntegerField()
    entrevistasInicialesPlaneadas = models.IntegerField()
    entrevistasInicialesRealizadas = models.IntegerField()
    entrevistasCierrePlaneadas = models.IntegerField()
    entrevistasCierreRealizadas = models.IntegerField()
    solicitudesSucritas = models.IntegerField()
