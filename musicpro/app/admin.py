from django.contrib import admin
from .models import Marca, Producto, Contacto, Categoria, Tipo_producto
# Register your models here.

admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Tipo_producto)
admin.site.register(Categoria)

