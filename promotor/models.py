from django.db import models
from django.contrib.auth.models import User
from productos.models import InstitucionFinanciera
from login.models import Persona
# Create your models here.

class promotorAsesor(models.Model):
    idAsesorPromotor = models.AutoField(primary_key=True)
    idAsesor = models.ForeignKey(Persona)
    idPromotor = models.ForeignKey(User)
    institucion = models.ForeignKey(InstitucionFinanciera)
    activo = models.NullBooleanField()
