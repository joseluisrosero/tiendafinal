from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import*

@receiver(post_save, sender=Producto)
def despues_de_guardar(sender, instance, created, **kwargs):
    if created:
        print(f'Se ha creado un nuevo producto: {instance.nombre}')
    else:
        print(f'Se ha actualizado el producto: {instance.nombre}')

@receiver(post_delete, sender=Producto)
def despues_de_eliminar(sender, instance, **kwargs):
    print(f'Se ha eliminado el producto: {instance.nombre}')