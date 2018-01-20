from __future__ import unicode_literals
from django.db import models
from login.models import Persona

class CatPais(models.Model):
    idPais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return(self.nombre)

class CatEstados(models.Model):
    idEstado = models.AutoField(primary_key=True)
    idPais   = models.ForeignKey(CatPais,null=False)
    nombre   = models.CharField(max_length=100)
    def __str__(self):
        return(self.nombre)

class Localidad(models.Model):
    idLocalidad = models.AutoField(primary_key=True)
    CatPais     = models.ForeignKey(CatPais,null=False)
    CatEstados  = models.ForeignKey(CatEstados,null=False)
    nombre      = models.CharField(max_length=200)
    def __str__(self):
        return(self.nombre)

class InstitucionFinanciera(models.Model):
    idInstitucion = models.AutoField(primary_key = True)
    idLocalidad   = models.ForeignKey(Localidad,null = False)
    idPersona     = models.ForeignKey(Persona, null = True, blank = True)
    nombre  = models.CharField(max_length=200, blank=True, null = True)
    calle   = models.CharField(max_length=100, blank=True, null = True)
    colonia = models.CharField(max_length=100, blank=True, null = True)
    cp      = models.CharField(max_length=5, blank=True, null = True)
    num_int = models.CharField(max_length=7, blank=True, null = True)
    num_ext = models.CharField(max_length=7, blank=True, null = True)
    def __str__(self):
        return(self.nombre +" "+self.calle)

class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key = True)
    idInstitucion  = models.ForeignKey(InstitucionFinanciera, null = False)
    nombre    = models.CharField(max_length=100, blank=True, null = True)
    ubicacion = models.CharField(max_length=50, blank=True, null = True)
    telefono  = models.CharField(max_length=15, blank=True, null = True)
    extension = models.CharField(max_length=5, blank=True, null = True)

    def __str__(self):
        return(self.nombre)

class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    idDepartamento = models.ForeignKey(Departamento,db_column='unique_together')
    nombrePlan = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return (self.nombrePlan)
