from django.urls import path
from . import views

app_name = 'catalogo'  # Namespace para hacer URLs reversibles

urlpatterns = [
    # Ruta para la vista basada en función (FBV)
    path('', views.home, name='home'),
    
    # Ruta para la vista basada en clase (CBV)
    path('productos/', views.ProductoListView.as_view(), name='producto_list'),
]