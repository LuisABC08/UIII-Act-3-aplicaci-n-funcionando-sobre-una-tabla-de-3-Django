from django.urls import path
from . import views

urlpatterns = [
    # Rutas principales
    path('', views.inicio_xbox, name='inicio'),
    
    # CRUD de Proveedores
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/ver/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedores/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),
]