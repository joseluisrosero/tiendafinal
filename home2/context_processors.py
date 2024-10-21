from .models import Categoria

def categorias_context_processor(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}
