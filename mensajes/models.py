from django.db import models
from cliente.models import AsesorCliente
# Create your models here


class Mensajes(models.Model):
    mensaje = models.CharField(max_length=240)
    asesorCliente = models.ForeignKey(AsesorCliente,blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    leido = models.BooleanField(default=False)
