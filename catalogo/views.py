from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto  # <-- Importante

def home(request):
    contexto = {
        'titulo': 'Bienvenido a la Tienda',
        'mensaje': 'Esta es la página principal construida con una FBV.',
        'anio': 2026
    }
    return render(request, 'catalogo/home.html', contexto)

class ProductoListView(ListView):
    model = Producto  # <-- Ahora sí usa el modelo
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Catálogo de Productos'
        context['subtitulo'] = 'Explora nuestros productos disponibles'
        context['anio'] = '2026'  # Para el filtro de fecha en la plantilla
        return context