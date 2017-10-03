from django.db import models
from login.models import Persona
from aseguradoras.models import Servicios
# Create your models here.


class Asesor(models.Model):
    idAsesor = models.OneToOneField(Persona,primary_key=True)
    tipoLicencia = models.PositiveIntegerField(blank=True, null=True)
    folio = models.CharField(max_length=15,blank=True,null=True)

class ReporteActividad(models.Model):
    idReporte = models.AutoField(primary_key=True)
    idAsesor = models.ForeignKey(Asesor)
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
