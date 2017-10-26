from django.contrib import admin

# Register your models here.

from .models import (
    Estatuscredito,
    Creditos,
    Sale
)
admin.site.register(Estatuscredito)
admin.site.register(Creditos)
admin.site.register(Sale)

# Register your models here.
