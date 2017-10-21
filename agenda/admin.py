from django.contrib import admin

# Register your models here.
from .models import (
    CatEstatuscita,
    CatTipocita,
    Cita,
)
admin.site.register(CatEstatuscita)
admin.site.register(CatTipocita)
admin.site.register(Cita)
