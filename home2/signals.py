from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import*

@receiver(post_save, sender=Producto)
def despues_de_guardar(sender, instance, created, **kwargs):
    if created:
        print(f'Se ha creado un nuevo producto: {instance.nombre}')
    else:
        print(f'Se ha actualizado el producto: {instance.nombre}')