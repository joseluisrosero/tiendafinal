from django.db.models.signals import*
from django.dispatch import receiver
from .models import*
from django.core.mail import send_mail

@receiver(post_save, sender=Producto)
def despues_de_guardar(sender, instance, created, **kwargs):
    if created:
        print(f'Se ha creado un nuevo producto: {instance.nombre}')
    else:
        print(f'Se ha actualizado el producto: {instance.nombre}') 


        

#post_save.disconnect(despues_de_guardar, sender=Producto)






"""@receiver(pre_save, sender=Producto)
def antes_de_guardar(sender, instance, **kwargs):
    if instance.pk:  # Si la instancia tiene una clave primaria, entonces ya existe en la base de datos
        print(f"El producto {instance.nombre} se va a actualizar")
    else:
        print(f"El producto {instance.nombre} se va a guardar por primera vez")


@receiver(post_save, sender=Producto)
def despues_de_guardar(sender, instance, created, **kwargs):
    if created:
        print(f'Se ha creado un nuevo producto: {instance.nombre}')
    else:
        print(f'Se ha actualizado el producto: {instance.nombre}')


@receiver(pre_delete, sender=Producto)
def antes_de_eliminar(sender, instance, **kwargs):
    print(f"Estás a punto de eliminar el producto: {instance.nombre}")


@receiver(post_delete, sender=Producto)
def despues_de_eliminar(sender, instance, **kwargs):
    print(f'Se ha eliminado el producto: {instance.nombre}')

@receiver(post_save, sender=Producto)
def enviar_correo_despues_de_guardar(sender, instance, created, **kwargs):
    if created:
        asunto = 'Nuevo producto creado'
        mensaje = f'Se ha creado un nuevo producto: {instance.nombre}'
    else:
        asunto = 'Producto actualizado'
        mensaje = f'Se ha actualizado el producto: {instance.nombre}'

    send_mail(
        asunto,
        mensaje,
        'roseroquicazanjoseluis@gmail.com',
        ['j.lucho9006@gmail.com']
    )"""
