from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Roles(models.Model):
    idRole = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

class EstadoCivil(models.Model):
    idEstadoCivil = models.PositiveIntegerField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=20,null=False)


    def __str__(self):
        return self.nombre

class CatTipodireccion(models.Model):
    idtipoDireccion = models.PositiveIntegerField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=50,null=False)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    curp = models.CharField(max_length=18)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    fechaDeNacimiento = models.CharField(max_length=10)
    idRol = models.ManyToManyField(Roles)
    folio = models.CharField(max_length=15)
    estadoCivil = models.OneToOneField(EstadoCivil,blank=True, null=True)

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            persona_profile = Persona.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)

class Contacto(models.Model):
    celular = models.AutoField(primary_key=True)
    idpersona = models.ForeignKey(Persona)
    email = models.CharField(max_length=60)
    telcasa = models.CharField(max_length=15)
    oficina = models.CharField(max_length=15, blank=True, null=True)
    facebookid = models.CharField(max_length=50, blank=True, null=True)



class Direccion(models.Model):
    iddireccion = models.AutoField(primary_key=True)
    idpersona = models.ManyToManyField(Persona)
    idtipodireccion = models.OneToOneField(CatTipodireccion)
    calle = models.CharField(max_length=150)
    colonia = models.CharField(max_length=100)
    delegacion = models.CharField(max_length=100)
    cp = models.CharField(max_length=5)
    numinterior = models.CharField(max_length=7, blank=True, null=True)
    numexterior = models.CharField(max_length=7)
