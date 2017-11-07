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
    user = models.OneToOneField(User)
    curp = models.CharField(max_length=18, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    fechaDeNacimiento = models.CharField(max_length=10, blank=True, null=True)
    idRol = models.ForeignKey(Roles,blank=True,null=True)
    estadoCivil = models.ForeignKey(EstadoCivil,null=True,blank=True)
    def create_profile(sender,**kwargs):
        if kwargs['created']:
            persona_profile = Persona.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)

    def __str__(self):
        return (self.user.first_name)

class Contacto(models.Model):
    celular = models.CharField(max_length=15)
    idpersona = models.ForeignKey(Persona,related_name='contacto')
    telcasa = models.CharField(max_length=15,blank=True,null=True)
    oficina = models.CharField(max_length=15,blank=True,null=True)
    facebookid = models.CharField(max_length=50, blank=True, null=True)

class Direccion(models.Model):
    iddireccion = models.AutoField(primary_key=True)
    idpersona = models.ForeignKey(Persona,related_name='direccion')
    idtipodireccion = models.ForeignKey(CatTipodireccion, null=True, blank=True)
    calle = models.CharField(max_length=150, blank=True, null=True)
    colonia = models.CharField(max_length=100, blank=True, null=True)
    delegacion = models.CharField(max_length=100, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    numinterior = models.CharField(max_length=7, blank=True, null=True)
    numexterior = models.CharField(max_length=7, blank=True, null=True)
