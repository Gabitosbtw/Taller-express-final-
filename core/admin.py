from django.contrib import admin
from .models import Empleado,Cliente,Factura,Pedido,Servicio,Proveedor,Vehiculo

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Pedido)
admin.site.register(Servicio)
admin.site.register(Proveedor)
admin.site.register(Vehiculo)