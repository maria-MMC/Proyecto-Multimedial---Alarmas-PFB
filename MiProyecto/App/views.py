# Create your views here.
from django.shortcuts import render , redirect, get_object_or_404
from App.models import *
from .forms import crear_Usuarios_forms, crearProductos_forms, crearDetallePedidoForms, UsuariosForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from App.models import MensajeContacto
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
from django.contrib.auth.models import User
# Create your views here.

def crearProductos(request):
    if request.method == "POST":
        form = crearProductos_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            productos = Producto(
                nombre=formulario_limpio['nombre'],
                descripcion=formulario_limpio['descripcion'],
                stock=formulario_limpio['stock']
            )
            productos.save()
            
            return render(request, "App/productos.html")
    
    else:
        form = crearProductos_forms()
    
    return render(request, 'App/crearProductos.html', {'form': form})

def crear_DetallePedido(request):
    if request.method == "POST":
        form = crearDetallePedidoForms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            detalle_pedido = DetallePedido(
                pedido=formulario_limpio["pedido"],
                producto=formulario_limpio["producto"],
                cantidad=formulario_limpio["cantidad"],
                precio_unitario=formulario_limpio["precio_unitario"],
                metodo_de_pago=formulario_limpio["metodo_de_pago"])
            detalle_pedido.save()
            return render(request, 'App/index.html')
    
    else:
        form = crearDetallePedidoForms()
    
    return render(request, 'App/crear_DetallePedido.html', {'form': form})

def buscar_nombre_producto(request):
    if request.GET.get('nombre',False):
        nombre = request.GET['nombre']
        Productos = Producto.objects.filter(nombre__icontains=nombre)

        return render(request,'App/buscar_nombre_producto.html',{'Productos':Productos})
    else:
        respuesta = 'No hay datos'
    return render(request,'App/buscar_nombre_producto.html',{'respuesta':respuesta})

def buscar_usuario(request):
    if request.GET.get('email',False):
        email = request.GET['email']
        usuarios = Usuarios.objects.filter(email__icontains=email)

        return render(request,'App/buscar_usuario.html',{'usuarios':usuarios})
    else:
        respuesta = 'No hay datos'
    return render(request,'App/buscar_usuario.html',{'respuesta':respuesta})

def buscar_metodo_de_pago(request):
    if request.GET.get('metodo_de_pago',False):
        metodo_de_pago = request.GET['metodo_de_pago']
        DetallePedidos = DetallePedido.objects.filter(metodo_de_pago__icontains=metodo_de_pago)

        return render(request,'App/buscar_metodo_de_pago.html',{'DetallePedidos':DetallePedidos})
    else:
        respuesta = 'No hay datos'
    return render(request,'App/buscar_metodo_de_pago.html',{'respuesta':respuesta})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        template = render_to_string('App/plantillaEmail.html',{
            'nombre': nombre,
            'email': email,
            'mensaje': mensaje,
            'asunto': asunto
        })
        emailSender = EmailMessage(
            asunto,
            template,
            settings.EMAIL_HOST_USER,
            ['mmilagroscarucci@gmail.com'], # Aca va el mail host que elegieron
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        try:
            emailSender.send()
        except Exception as e:
            messages.error(request, f'Error al enviar el mensaje: {str(e)}')
            return redirect('contacto')  # Redirect back to the contact page

        if nombre and email and mensaje:
            # Guardar el mensaje en la base de datos
            MensajeContacto.objects.create(
                nombre=nombre,
                email=email,
                mensaje=mensaje,
            )

            # Enviar confirmación al usuario
            send_mail(
                'Gracias por contactarnos ',
                f'Hola {nombre}, hemos recibido tu mensaje y te contactaremos pronto.',
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )

            messages.success(request, 'Mensaje enviado exitosamente.')
            return redirect('agradecimiento')
        else:
            messages.error(request, 'Por favor, completa todos los campos.')

    return render(request, 'App/contacto.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            user_django = User.objects.create_user(
                username=usuario.nombre,
                email=usuario.email,
                password=usuario.contraseña
            )
            messages.success(request, 'Registro exitoso! Bienvenido/a')
            return render(request, 'App/index.html')
    else:
            form = UsuariosForm()
    
    return render(request, 'App/registro.html', {'form': form})
    

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)
        

            if user is not None:
                login(request, user)

                return render(request, "App/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:

                return render(request, "App/index.html", {"mensaje":"Error, datos incorrectos"})

        else:

                return render(request,"App/index.html" , {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "App/login.html" , {'form':form})

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Cambia 'index' por el nombre de tu url principal
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'App/login.html')

def logout_request(request):
    logout(request)
    return render(request, "App/index.html", {"mensaje": "Has cerrado sesion exitosamente"})

def eliminar_productos(request, productos_id):
    productos = Producto.objects.get(id=productos_id)
    productos.delete()

    return redirect('productos')

def actualizar_productos(request,productos_id):
    productos = Producto.objects.get(id=productos_id)
    if request.method == "POST":
        form = crearProductos_forms(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            productos.nombre = data['nombre']
            productos.descripcion=data['descripcion']
            productos.stock=data['stock']
            productos.save()

            return redirect('productos')
    else:
        form = crearProductos_forms(initial={'nombre':productos.nombre, 'descripcion':productos.descripcion, 'stock':productos.stock})
    
    return render(request, 'App/actualizar_productos.html', {'form':form, 'producto':productos})

def eliminar_usuarios(request, usuarios_id):
    usuarios = Usuarios.objects.get(id=usuarios_id)
    usuarios.delete()

    usuario = usuarios.objects.all()
    context = {'usuario':usuario}

    return render(request,'App/index.html',context=context)

def actualizar_usuarios(request,usuario_id):
    usuario = Usuarios.objects.get(id=usuario_id)
    if request.method == "POST":
        form = crear_Usuarios_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            usuario.nombre = formulario_limpio['nombre']
            usuario.email=formulario_limpio['email']
            usuario.contraseña=formulario_limpio['contraseña']
            usuario.celular=formulario_limpio['celular']
            usuario.save()

            return render(request,'App/index.html')
    else:
        form = crearProductos_forms(initial={'nombre':usuario.nombre, 'email':usuario.email, 'contraseña':usuario.contraseña, 'celular':usuario.celular})
    
    return render(request, 'App/actualizar_usuarios.html', {form:form})

def eliminar_detalles(request, detalles_id):
    detalles = DetallePedido.objects.get(id=detalles_id)
    detalles.delete()

    detalle = detalle.objects.all()
    context = {'detalle':detalle}

    return render(request,'App/index.html',context=context)

def actualizar_detalles(request,detalles_id):
    detalle = DetallePedido.objects.get(id=detalles_id)
    if request.method == "POST":
        form = crearDetallePedidoForms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data
            detalle.pedido = formulario_limpio['pedido']
            detalle.producto=formulario_limpio['producto']
            detalle.cantidad=formulario_limpio['cantidad']
            detalle.precio_unitario=formulario_limpio['precio_unitario']
            detalle.metodo_de_pago=formulario_limpio['metodo_de_pago']
            detalle.save()

            return render(request,'App/index.html')
    else:
        form = crearDetallePedidoForms(initial={'pedido':detalle.pedido, 'producto':detalle.producto, 'cantidad':detalle.cantidad, 'precio_unitario':detalle.precio_unitario, 'metodo_de_pago':detalle.metodo_de_pago})
    
    return render(request, 'App/actualizar_detalles.html', {form:form})

def guia(request):
    pasos = range(1, 6)  # Genera los números del 1 al 5
    return render(request, 'App/guia.html', {'pasos': pasos})

def home(request):
    return render(request, 'App/index.html')

def faq(request):
    return render(request, 'App/faq.html')

def productos(request):
    producto = Producto.objects.all()
    context = {'producto':producto}
    return render(request, 'App/productos.html',context=context)

def usuarios(request):
    usuario = Usuarios.objects.all()
    context = {'usuario':usuario}
    return render(request, 'App/usuarios.html',context=context)

def detalles(request):
    detalle = DetallePedido.objects.all()
    context = {'detalle':detalle}
    return render(request, 'App/detalles.html',context=context)

def agradecimiento(request):
    return render(request, 'App/agradecimiento.html')

def sobreNosotros(request):
    return render(request, 'App/sobreNosotros.html')

def soporte(request):
    return render(request, 'App/soporte.html')

def politica_privacidad(request):
    return render(request, 'App/politica_privacidad.html')

def terminosYCondiciones(request):
    return render(request, 'App/terminosYCondiciones.html')

def carrito(request):
    return render(request, 'App/carrito.html')