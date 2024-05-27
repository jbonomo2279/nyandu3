from django.contrib import admin
from .models import Pais, Provincia, Aeropuerto, Fabricante, Modelo, Avion, Empleado, Vuelo, Categoria

# Register your models here.

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Aeropuerto)
admin.site.register(Fabricante)
admin.site.register(Modelo)
admin.site.register(Avion)
admin.site.register(Empleado)
admin.site.register(Vuelo)
admin.site.register(Categoria)
