from django.db import models

# Create your models here.

class CatPais(models.Model):
    idPais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class CatEstados(models.Model):
    idEstado = models.IntegerField()
    idPais = models.OneToOneField(CatPais,primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class Localidades(models.Model):
    idLocalidad = models.AutoField(primary_key=True)
    catEstadoEstado = models.OneToOneField(CatEstados)
    nombre = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class Institucionfinanciera(models.Model):
    idInstitucionFinanciera = models.AutoField(primary_key=True)  # Field name made lowercase.
    idLocalidad = models.ForeignKey(Localidades,db_column='idlocalidad')
    nombre = models.CharField(max_length=200)
    calle = models.CharField(max_length=100)
    coloniaMunicipio = models.CharField(max_length=100)
    cp = models.CharField(max_length=5)
    numExterior = models.CharField(max_length=7)
    numeroInterior = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class Departamento(models.Model):
    idDepartamento = models.IntegerField(primary_key=True)
    idInstitucionFinanciera = models.ManyToManyField(Institucionfinanciera)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    extension = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class Servicios(models.Model):
    idServicio = models.AutoField(primary_key=True)
    idDepartamento = models.ManyToManyField(Departamento)
    nombrePlan = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return (self.nombre,self.descripcion)
