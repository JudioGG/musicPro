from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields import NullBooleanField

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Tipo_producto(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Categoria(models.Model):
    
    categoria_producto = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria_producto

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo_prod = models.ForeignKey(Tipo_producto, on_delete=models.PROTECT)
    categoria_prod = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos",   null=True) 
    def __str__(self):
        return self.nombre

opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre