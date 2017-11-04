from django.db import models
from django.contrib.auth.models import User
from productos.models import Institucionfinanciera
from login.models import Persona
# Create your models here.

class promotorAsesor(models.Model):
    idAsesor = models.ForeignKey(Persona)
    idPromotor = models.ForeignKey(User)
    institucion = models.ForeignKey(Institucionfinanciera)
