from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponseRedirect
from .forms import agregar_producto_form, login_form, contacto_form, register_form
from .models import Producto, Categoria, Marca
from .utils.utils import resize_and_compress_image
import os
import sys
from django.contrib.auth.decorators import login_required
from .log_manager import LogManager




@login_required
def vista_agregar_producto(request):
    if request.method == 'POST':
        print(f"User '{request.user.username}' is authenticated and submitting a product.")
        
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            prod = formulario.save(commit=False)
            prod.status = True
            prod.save()
            formulario.save_m2m()
            
            if 'imagen' in request.FILES:
                image = request.FILES['imagen']
                output_path = os.path.join('media/productos', image.name)
                resize_and_compress_image(image, output_path)
            
            return redirect('vista_lista_producto')
    else:
        formulario = agregar_producto_form()
    
    return render(request, 'vista_agregar_producto.html', locals())





# Create your views here.

def vista_lista_producto (request):
    lista = Producto.objects.filter()
    logger = LogManager()
    logger.log_info("Lista de productos cargada correctamente.")
    return render(request, 'lista_producto.html',locals())

def vista_about(request):
    return render(request,'about.html')

def vista_funko(request):
    return render(request,'funko.html')

def vista_contacto(request):
    info_enviado = False
    email = ""
    title = ""
    texto = ""
    if request.method =="POST":
        formulario =contacto_form(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['correo']
            title = formulario.cleaned_data['titulo']
            texto = formulario.cleaned_data['texto']
    else: #si es metodo GET u otro metodo
        formulario= contacto_form()    
    return render(request,'contacto.html',locals())

def vista_home(request):
    productos_nuevos = Producto.objects.filter(status=True).order_by('-id')[:4]
    
    return render(request, 'home.html', {'productos_nuevos': productos_nuevos})



"""@login_required
def vista_agregar_producto(request):
    if not request.user.is_authenticated:
        print("User is not authenticated.")
    else:
        print(f"User '{request.user.username}' is authenticated.")

    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            prod = formulario.save(commit=False)
            prod.status = True
            prod.save()
            formulario.save_m2m()
            # Obtener la imagen cargada y la ruta de guardado
            image = request.FILES['imagen']
            output_path = os.path.join('media/productos', image.name)
            # Redimensionar y comprimir la imagen
            resize_and_compress_image(image, output_path)

            return redirect('vista_lista_producto')
    else:
        formulario = agregar_producto_form()
    return render(request, 'vista_agregar_producto.html', locals())
"""
def vista_ver_producto(request, id_prod):
    p = Producto.objects.get(id=id_prod)
    return render(request,'ver_producto.html',locals())



@login_required
def vista_editar_producto(request, id_prod):
    prod = Producto.objects.get(id=id_prod)
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES, instance=prod)
        if formulario.is_valid():
            if 'imagen-clear' in request.POST:  
                if prod.imagen:
                    prod.imagen.delete(save=False)
                prod.imagen =None

            prod = formulario.save(commit=False)
     
      
      
            if 'imagen' in request.FILES: 
                image = request.FILES['imagen']     
                img_io = resize_and_compress_image(image) 
            
                if img_io: 
                    image_name = image.name 
                    prod.imagen = InMemoryUploadedFile( img_io, 
                        field_name='imagen', 
                        name=image_name, 
                        content_type=image.content_type, 
                        size=sys.getsizeof(img_io), 
                        charset=None )
            
        prod.save()

        if formulario.cleaned_data.get('categorias'):
                formulario.save_m2m()

        return redirect('vista_ver_producto', id_prod=prod.id)
               
    else: 
        formulario = agregar_producto_form(instance = prod)
    return render(request, 'vista_editar_producto.html',locals())



@login_required
def vista_eliminar_producto(request, id_prod):
    prod = get_object_or_404(Producto, id=id_prod)
    if request.method == 'POST':
        prod.delete()
        return redirect('vista_lista_producto')
    return render(request, 'confirmar_eliminar_producto.html', {'producto': prod})




def vista_login(request):
    mensaje = ""
    next_url = request.GET.get('next', request.POST.get('next', '/'))

    if not next_url or next_url == '/':
        next_url = request.META.get('HTTP_REFERER', '/home/')

    if request.method == "POST":
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            user = authenticate(username=usu, password=cla)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print(f"User '{user.username}' logged in successfully. Redirecting to {next_url}")
                    return redirect(next_url)  # Asegúrate de redirigir a next_url
                else:
                    mensaje = 'Cuenta desactivada.'
                    print("User account is deactivated.")
            else:
                mensaje = 'Usuario o clave incorrectos.'
                print("Authentication failed: Invalid username or password.")
    else:
        formulario = login_form()

    print(f"Rendering login form. Next URL: {next_url}")
    return render(request, 'login.html', {'formulario': formulario, 'mensaje': mensaje, 'next': next_url})





def vista_logout (request):
    logout(request)
    next = request.GET.get('next' , '/')
    return HttpResponseRedirect(next)

def vista_register(request):
    formulario = register_form()
    if request.method == 'POST':
        formulario = register_form(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            correo = formulario.cleaned_data['email']
            password_1 = formulario.cleaned_data['password_1']
            password_2 = formulario.cleaned_data['password_2']
            u = User.objects.create_user(username=usuario, email=correo, password=password_1)
            u.save()
            return render(request, 'thanks_for_register.html', locals())
        else:
            return render(request, 'register.html', locals())
    return render(request, 'register.html', locals())

def base_view(request):
    categorias = Categoria.objects.all()
    return render(request, 'base.html', {'categorias': categorias})


def productos_por_marca(request, marca_id):
    marca = Marca.objects.get(id=marca_id)
    productos = Producto.objects.filter(marca=marca)
    return render(request, 'productos_por_marca.html', {'productos': productos, 'marca': marca})

def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria)
    return render(request, 'productos_por_categoria.html', {'productos': productos, 'categoria': categoria})


