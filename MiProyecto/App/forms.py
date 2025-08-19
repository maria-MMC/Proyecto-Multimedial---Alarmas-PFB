from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm


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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}

class LoginForm(AuthenticationForm):
    usuario = forms.CharField(widget=TextInput())
    contraseña = forms.CharField(widget=PasswordInput())