from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class CatPais(models.Model):
    idPais = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class CatEstados(models.Model):
    idEstado = models.AutoField(primary_key=True)
    idPais = models.OneToOneField(CatPais, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class Localidades(models.Model):
    idLocalidad = models.AutoField(primary_key=True)
    catEstadoEstado = models.OneToOneField(CatEstados,  on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class Institucionfinanciera(models.Model):
    idInstitucionFinanciera = models.AutoField(primary_key=True)  # Field name made lowercase.
    idLocalidad = models.ForeignKey(Localidades,db_column='idlocalidad',  on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    calle = models.CharField(max_length=100)
    coloniaMunicipio = models.CharField(max_length=100)
    cp = models.CharField(max_length=5)
    numExterior = models.CharField(max_length=7)
    numeroInterior = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return (self.nombre)

class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True)
    idInstitucionFinanciera = models.ForeignKey(Institucionfinanciera,db_column='idInstitucionFinanciera',  on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15)
    extension = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        unique_together = ('idDepartamento','idInstitucionFinanciera')

    def __str__(self):
        return (self.nombre)

class Servicios(models.Model):
    idServicio = models.AutoField(primary_key=True)
    idDepartamento = models.ForeignKey(Departamento,db_column='unique_together',  on_delete=models.CASCADE)
    nombrePlan = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return (self.nombrePlan)

class EstadoCivil(models.Model):
    idEstadoCivil = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=20,null=False)


    def __str__(self):
        return self.nombre


class Roles(models.Model):
    idRole = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    curp = models.CharField(max_length=18, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    fechaDeNacimiento = models.CharField(max_length=10, blank=True, null=True)
    idRol = models.ForeignKey(Roles,blank=True,null=True, on_delete=models.CASCADE)
    estadoCivil = models.ForeignKey(EstadoCivil,null=True,blank=True, on_delete=models.CASCADE)
    def create_profile(sender,**kwargs):
        if kwargs['created']:
            persona_profile = Persona.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)

    def __str__(self):
        return (self.user.first_name)

class PlanesConcretados(models.Model):
    idPlan = models.AutoField(primary_key=True)
    idAsesor = models.ForeignKey(User,on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Persona,on_delete=models.CASCADE)
    idServicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    fechaContratacion = models.DateField()
    numeroPoliza = models.CharField(max_length=10)
    primaNetaAnual = models.FloatField()
    plazoAnos = models.IntegerField()
    valorPlan = models.FloatField()
    observaciones = models.CharField(max_length=300, blank=True, null=True)
