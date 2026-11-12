from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Esto sirve para que en el admin o en la consola se vea el nombre del producto
        return self.nombre