from django.contrib import admin
from django.urls import path, include  # <-- Agregamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos las rutas de nuestra app 'catalogo'
    path('', include('catalogo.urls')), 
]