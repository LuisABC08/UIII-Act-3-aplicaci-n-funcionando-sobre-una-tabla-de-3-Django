from django.db import models

# ==========================================
# MODELO: PROVEEDOR (Equivalente a Categoria para el CRUD inicial)
# ==========================================
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)  # Se asume auto-incrementable
    nombre = models.CharField(max_length=150) # varchar
    contacto = models.CharField(max_length=150, blank=True, null=True) # varchar
    telefono = models.CharField(max_length=20, blank=True, null=True) # varchar
    email = models.EmailField(max_length=100, blank=True, null=True) # varchar (se usa EmailField)
    direccion = models.CharField(max_length=255, blank=True, null=True) # varchar
    activo = models.BooleanField(default=True) # boolean
    fecha_registro = models.DateTimeField(auto_now_add=True) # datetime (se usa auto_now_add)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: VIDEOJUEGO
# ==========================================
class Videojuego(models.Model):
    id_videojuego = models.AutoField(primary_key=True) # Se asume auto-incrementable
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, related_name="videojuegos") # Relación con Proveedor
    titulo = models.CharField(max_length=255) # varchar
    genero = models.CharField(max_length=100) # varchar
    plataforma = models.CharField(max_length=100) # varchar
    precio = models.DecimalField(max_digits=10, decimal_places=2) # decimal
    fecha_lanzamiento = models.DateField() # date
    desarrollador = models.CharField(max_length=150) # varchar

    def __str__(self):
        return self.titulo

# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True) # Se asume auto-incrementable
    id_videojuego = models.ForeignKey(Videojuego, on_delete=models.PROTECT, related_name="ventas") # Relación con Videojuego
    total_venta = models.DecimalField(max_digits=10, decimal_places=2) # decimal
    fecha_venta = models.DateTimeField(auto_now_add=True) # datetime (se usa auto_now_add)
    cliente_nombre = models.CharField(max_length=255) # varchar
    metodo_pago = models.CharField(max_length=50) # varchar
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) # decimal
    observaciones = models.TextField(blank=True, null=True) # text

    def __str__(self):
        return f"Venta {self.id_venta} - {self.cliente_nombre}"