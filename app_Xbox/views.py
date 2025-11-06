from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor

# ==========================================
# FUNCIONES DE VISTAS
# ==========================================

# 1. Vista de Inicio (Inicio del sistema)
def inicio_xbox(request):
    return render(request, 'inicio.html')

# 2. Agregar Proveedor (GET para mostrar el formulario, POST para guardar)
def agregar_proveedor(request):
    if request.method == 'POST':
        # No se usa forms.py - se lee directamente del POST
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        activo = request.POST.get('activo', 'off') == 'on' # Checkbox activo

        Proveedor.objects.create(
            nombre=nombre,
            contacto=contacto,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=activo,
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

# 3. Ver Proveedores (Listar todos)
def ver_proveedores(request):
    proveedores = Proveedor.objects.all().order_by('nombre')
    context = {'proveedores': proveedores}
    return render(request, 'proveedor/ver_proveedores.html', context)

# 4. Actualizar Proveedor (GET para mostrar datos, POST para guardar)
def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        # Leer datos del POST y actualizar el objeto
        proveedor.nombre = request.POST.get('nombre')
        proveedor.contacto = request.POST.get('contacto')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.activo = request.POST.get('activo', 'off') == 'on'
        proveedor.save()
        return redirect('ver_proveedores')

    # GET request
    context = {'proveedor': proveedor}
    return render(request, 'proveedor/actualizar_proveedor.html', context)

# 5. Borrar Proveedor (Solo POST para la acción de borrado)
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    
    # GET request para mostrar la confirmación
    context = {'proveedor': proveedor}
    return render(request, 'proveedor/borrar_proveedor.html', context)