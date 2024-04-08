
from django.contrib import admin
from .models import Gasto, Presupuesto, Ingreso

admin.site.register(Gasto)
admin.site.register(Presupuesto)
admin.site.register(Ingreso)