from django.urls import path 
from .views import*


urlpatterns = [
    
    path('', vista_home, name='home'),
    path('home/', vista_home, name='home'),
    path('about/',vista_about),
    path('funko', vista_funko, name='funko'),
    path('contacto/',vista_contacto,name='vista_contacto'),   
    path('lista_producto/',vista_lista_producto,name='vista_lista_producto'),
    path('agregar_producto/',vista_agregar_producto,name='vista_agregar_producto'),
    path('ver_producto/<int:id_prod>/', vista_ver_producto,name='vista_ver_producto'),
    path('editar_producto/<int:id_prod>/', vista_editar_producto,name='vista_editar_producto'),
    path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto,name='vista_eliminar_producto'),
    path('login/',vista_login, name='vista_login'),
    path('logout/',vista_logout, name='vista_logout'),
    path('register/',vista_register, name='vista_register'),
    path('marca/<int:marca_id>/', productos_por_marca, name= 'productos_por_marca'),
    path('categoria/<int:categoria_id>/', productos_por_categoria, name= 'productos_por_categoria'),
    path('eliminar_producto/<int:id_prod>/', vista_eliminar_producto, name='vista_eliminar_producto')

]

