from __future__ import unicode_literals

from django.db import models
from cliente.models import AsesorCliente
from login.models import Persona
from django.conf import settings
from django.contrib.auth.models import User


class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)
        conekta.api_key = settings.CONEKTA_PUBLIC_KEY
 #request.user.first_name,request.user.email
    def charge(self,token_id,cantidad):
        total = 0
        print("model: ",cantidad,type(cantidad))
        for i in range(0,cantidad):
            total = total + 20000
        try:
            order = conekta.Order.create({
            "line_items": [
            {
                "name": "Creditos",
                "description": "Creditos de Vive Tu futuro.",
                "unit_price": 20000,
                "quantity": cantidad,
            }],
            "customer_info":{
                "name": "nombre",
                "phone": "+52553344556",
                "email": "eckobik@gmail.com",
                "corporate": False,
                "vertical_info": {}
            },
            "charges": [{
                "payment_method":{
                "type": "card",
                "token_id": token_id
                },
                "amount": total
            }],
            "currency" : "mxn",
            "metadata" : {"test" : "extra info"}
            })
            print(order.id)

        except conekta.ConektaError as e:
            return e.error_json['message']


class Estatuscredito(models.Model):
    idestatuscredito = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Creditos(models.Model):
    idCredito = models.AutoField(primary_key=True)
    estatusCredito = models.ForeignKey(Estatuscredito, blank=True, null=True)
    idAsesor = models.ForeignKey(User)
    idCliente = models.OneToOneField(AsesorCliente, blank=True, null=True)
