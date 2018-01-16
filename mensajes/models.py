from django.db import models
from login.models import Persona
from django.contrib.auth.models import User
# Create your models here


class Mensajes(models.Model):
    mensaje = models.CharField(max_length=240)
    de = models.ForeignKey(Persona)
    para = models.ForeignKey(User)
    fecha = models.DateTimeField()
    leido = models.BooleanField(default=False)
