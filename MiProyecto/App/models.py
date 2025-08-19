from django.db import models
from django.utils import timezone

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return f"Usuario: {self.nombre}" 

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Assuming Pedido has a foreign key to Usuario
        # and you want to display the user's name along with the order ID
        return f"Pedido {self.id} - {self.usuario.nombre}"
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_de_pago = {
        ('Efectivo','Efectivo'),
        ('Tarjeta','Tarjeta'),
        ('Transferencia','Transferencia'),
        ('Paypal','Paypal'),
        ('Criptomoneda','Criptomoneda'),
    }
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Pedido {self.pedido.id})"
    

class Garantia(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Mensaje de {self.producto.nombre} desde {self.fecha_inicio} hasta {self.fecha_fin}"

class MetodoDeEnvio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200, default='Sin asunto')
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Mensaje de {self.nombre} - {self.email}'