from django.shortcuts import render,redirect
from .forms import*
from .models import*



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