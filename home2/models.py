import os
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    status = models.BooleanField(default= True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True) 


    def __str__(self):
        return self.nombre
    
    def formatted_precio(self):
        return "${:,.0f}".format(self.precio)
    
    def delete(self, *args, **kwargs):

        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super().delete(*args, **kwargs)
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id} de {self.usuario.nombre}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
    
class perfil (models.Model):
    user    =models.OneToOneField(User, on_delete=models.CASCADE)
    foto    =models.ImageField(upload_to='perfiles' , null=True,  blank=True)
    nombre  =models.CharField(max_length= 100)