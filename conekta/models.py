from django.db import models
from cliente.models import AsesorCliente
from asesor.models import Asesor
# Create your models here.
from django.conf import settings
import conekta
import json

class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)
        conekta.api_key = settings.CONEKTA_PRIVATE_KEY

    def charge(self, price_in_cents, token_id, total,user,email):
        try:
            charge = conekta.Charge.create({
              "description":"Stogies",
              "amount": price_in_cents,
              "currency":"MXN",
              "reference_id":"1_credito",
              "card": token_id,
              "details": {
                "name": user,
                "email": email,
                "line_items": [{
                  "name": "Credito de Asesor",
                  "description": "",
                  "unit_price": price_in_cents,
                  "quantity": total,
                  "sku": "cohb_s1",
                  "category": "credit"
                }],
                "shipment": {
                    "carrier":"ViveTuFuturo",
                    "service":"Local",
                    "price": price_in_cents,
                  }
              }
            })
            return json.dumps(charge.__dict__)
        except conekta.ConektaError as e:
            return e.error_json['message']


class Estatuscredito(models.Model):
    idestatuscredito = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return (self.nombre,self.descripcion)

class Creditos(models.Model):
    idCredito = models.AutoField(primary_key=True)
    estatusCredito = models.OneToOneField(Estatuscredito)
    idAsesor = models.ForeignKey(Asesor,on_delete=models.CASCADE)
    idCliente = models.OneToOneField(AsesorCliente, blank=True, null=True)
