from django.contrib import admin
from .models import Administrador, SolicitudPresupuesto, Presupuesto, Costo


admin.site.register(Administrador)
admin.site.register(SolicitudPresupuesto)
admin.site.register(Presupuesto)
admin.site.register(Costo)