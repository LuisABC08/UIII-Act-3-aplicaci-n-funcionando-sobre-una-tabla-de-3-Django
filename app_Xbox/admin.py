from django.contrib import admin
from .models import Proveedor, Videojuego, Venta

# Solo trabajaremos inicialmente con Proveedor
admin.site.register(Proveedor)

# Se dejan pendientes:
# admin.site.register(Videojuego)
# admin.site.register(Venta)