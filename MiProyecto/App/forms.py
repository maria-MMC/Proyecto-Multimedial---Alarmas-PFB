from django import forms
from .models import *
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm

#preguntar: la pagina es de admin o de comprador? o ambas?
#           boton de login
#crear dos o tres botones:
#1. crear pedido:
#   redirigirte a otra pagina donde puedas cargar los datos del pedido.
#   por ejemplo: nombre de usuario, nombre del producto, cantidad, email, forma de pago
#2. editar pedido/finalizar compra:
#   redirigir al carrito donde confirma o cancela la compra.

class crear_Usuarios_forms(forms.Form):
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=100)
    celular = forms.CharField(max_length=20)

class crearProductos_forms(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(widget=forms.Textarea)
    stock = forms.IntegerField()

class crearDetallePedidoForms(forms.Form):
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

class MensajeContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    email = forms.EmailField(label="Email")
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")
    fecha_envio = forms.DateTimeField(label="Fecha de envío")

class UsuariosForm(forms.ModelForm):
    email = forms.EmailField()
    contraseña = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuarios
        fields = [
            'nombre',
            'email',
            'contraseña'
        ]
        help_texts = {k: '' for k in fields}

class LoginForm(AuthenticationForm):
    usuario = forms.CharField(widget=TextInput())
    contraseña = forms.CharField(widget=PasswordInput())