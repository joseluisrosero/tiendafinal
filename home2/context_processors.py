from .models import*

def categorias_context_processor(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}

def marcas_context_processor(request):
    marcas = Marca.objects.all()
    return {'marcas': marcas}
