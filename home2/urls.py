from django.urls import path 
from .views import*

urlpatterns = [

    path('home', vista_home, name='home'),
    path('about/',vista_about),
    path('funko', vista_funko, name='funko'),
    path('contacto/',vista_contacto,name='vista_contacto'),   
    path('lista_producto/',vista_lista_producto,name='vista_lista_producto'),
    path('agregar_producto/',vista_agregar_producto,name='vista_agregar_producto'),
    path('ver_producto/<int:id_prod>/', vista_ver_producto,name='vista_ver_producto'),
    path('editar_producto/<int:id_prod>/', vista_editar_producto,name='vista_editar_producto'),
    path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto,name='vista_eliminar_producto'),
    
]

