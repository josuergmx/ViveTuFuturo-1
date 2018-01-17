from django.db import models
from cliente.models import AsesorCliente
# Create your models here


class Mensajes(models.Model):
    mensaje = models.CharField(max_length=240)
    asesorCliente = models.ForeignKey(AsesorCliente)
    fecha = models.DateTimeField()
    tipo = models.IntegerField()
    leido = models.BooleanField(default=False)
