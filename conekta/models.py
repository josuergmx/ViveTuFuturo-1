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
        conekta.locale = 'es'
    def charge(self, price_in_cents, token_id, total,user,email):
        try:
            order = conekta.Order.create({
            "line_items": [
            {
                "name": "Box of Cohiba S1s",
                "description": "Imported From Mex.",
                "unit_price": 20000,
                "quantity": 1,
                "sku": "cohb_s1",
                "category": "food",
                "type" : "physical",
                "tags" : ["food", "mexican food"]
            }],
            "shipping_lines":[
            {
                "amount": 0,
                "tracking_number": "TRACK123",
                "carrier": "USPS",
                "method": "Train",
            "metadata": {
                "random_key": "random_value"
            }
            }],
            "customer_info":{
                "name": "John Constantine",
                "phone": "+525533445566",
                "email": "john@meh.com",
                "corporate": False,
                "vertical_info": {}
            },
            "shipping_contact":{
                "phone" : "5544332211",
                "receiver": "Marvin Fuller",
                "between_streets": "Ackerman Crescent",
                "address": {
                    "street1": "250 Alexis St",
                    "state": "Alberta",
                    "country": "MX",
                    "postal_code": "23455",
                    "metadata":{ "soft_validations": True}
                }
            },
            "charges": [{
                "payment_method":{
                "type": "card",
                "token_id": token_id
                },
                "amount": 20000
            }],
            "currency" : "mxn",
            "metadata" : {"test" : "extra info"}
        })
            return json.dumps(charge.__dict__)
        except conekta.ConektaError as e:
            print(e.message)


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
