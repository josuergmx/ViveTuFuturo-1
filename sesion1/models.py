from django.db import models
from cliente.models import AsesorCliente
# Create your models here.
# Create your models here.


class Blindajefinanciero(models.Model):
    idbl = models.AutoField(primary_key=True)
    column = models.IntegerField(blank=True, null=True)  # Field name made lowercase.

class Capitalizacion(models.Model):
    idcapitalizacion = models.AutoField(primary_key=True)
    column = models.IntegerField(blank=True, null=True)  # Field name made lowercase.

#Esta tabla cambiarà a Plan, donde iràn los datos ejes de edad, edad final, ahorro, grantotal.
class Libertadfinanciera(models.Model):
    idlf = models.AutoField(primary_key=True)
    edad = models.IntegerField(blank=True, null=True)
    montoObjetivo = models.IntegerField(blank=True, null=True)
    anos = models.IntegerField(blank=True, null=True)
    ahorro = models.FloatField(blank=True, null=True)

#Agregar tabla objetivos donde obtendremos los datos para calculas grantotal.
class Sesion1(models.Model):
    idSesion = models.AutoField(primary_key=True)
    idAsesorCliente = models.OneToOneField(AsesorCliente)
    videoPresentacion = models.CharField(max_length=100, blank=True, null=True)
    cartaConfidencialidad = models.CharField(max_length=100, blank=True, null=True)
    libertadFinancieraiDlf = models.ForeignKey(Libertadfinanciera)
    idCapitalizacion = models.ForeignKey(Capitalizacion)
    blindajeFinancieroidbl = models.ForeignKey(Blindajefinanciero)
