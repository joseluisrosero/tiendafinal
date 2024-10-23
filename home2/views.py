from django.shortcuts import render,redirect
from .forms import*
from .models import*
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def vista_lista_producto (request):
    lista = Producto.objects.filter()
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
    return render(request, 'home.html')


def vista_agregar_producto(request):
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            prod = formulario.save(commit=False)
            prod.status = True
            prod.save()
            formulario.save_m2m()
            return redirect('/lista_producto/')
    else: 
        formulario = agregar_producto_form()
    return render(request, 'vista_agregar_producto.html',locals())

def vista_ver_producto(request, id_prod):
    p = Producto.objects.get(id=id_prod)
    return render(request,'ver_producto.html',locals())

def vista_editar_producto(request, id_prod):
    prod = Producto.objects.get(id=id_prod)
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES, instance=prod)
        if formulario.is_valid():
            prod = formulario.save()
            return redirect ('vista_ver_producto',id_prod=prod.id)
    else: 
        formulario = agregar_producto_form(instance = prod)
    return render(request, 'vista_editar_producto.html',locals())

def vista_eliminar_producto(request, id_prod):
    prod = Producto.objects.get(id=id_prod)
    prod.delete()
    return redirect ('/lista_producto')


def vista_login (request):
    usu = ""
    cla = ""
    if request.method == "POST":
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            Usuario = authenticate(usurname=usu, password=cla)
            if   Usuario is not None and Usuario.is_activate:
                 login(request, Usuario)
                 return redirect('/')
            else:
                msj = "usuario o clave incorrectos"
    formulario = login_form()
    return render(request, 'login.html', locals())

def vista_logout (request):
    logout(request)
    return redirect('/login')

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

