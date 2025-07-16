from django.urls import path
from . import views
from App import views

urlpatterns = [
    path('', views.home, name = 'home'), 
    path('contacto/', views.contacto, name = 'contacto'),
    path('guia/', views.guia, name ='guia'),
    path('productos/', views.productos, name ='productos'),
    path('usuarios/', views.usuarios, name ='usuarios'),
    path('detalles/', views.detalles, name ='detalles'),
    path('faq/', views.faq, name ='faq'),
    path('crearProductos/', views.crearProductos, name = 'crearProductos'),
    path('crear_DetallePedido/', views.crear_DetallePedido, name = 'crear_DetallePedido'),
    path('agradecimiento/', views.agradecimiento, name='agradecimiento'),
    path('sobreNosotros/', views.sobreNosotros, name='sobreNosotros'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('soporte/', views.soporte, name='soporte'),
    path('politica_privacidad/', views.politica_privacidad, name='politica_privacidad'),
    path('terminosYCondiciones/', views.terminosYCondiciones, name='terminosYCondiciones'),
    path('registro/', views.registro_usuario, name='Registro'),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.logout_request, name='logout'),
    path('buscar_nombre_producto/', views.buscar_nombre_producto, name='buscar_nombre_producto'),
    path('buscar_usuario/', views.buscar_usuario, name='buscar_usuario'),
    path('buscar_metodo_de_pago/', views.buscar_metodo_de_pago, name='buscar_metodo_de_pago'),
    path('eliminar_usuarios/<usuarios_id>', views.eliminar_usuarios, name='eliminar_usuarios'),
    path('eliminar_productos/<productos_id>', views.eliminar_productos, name='eliminar_productos'),
    path('eliminar_detalles/<detalles_id>', views.eliminar_detalles, name='eliminar_detalles'),
    path('actualizar_detalles/<detalles_id>', views.actualizar_detalles, name='actualizar_detalles'),
    path('actualizar_productos/<productos_id>', views.actualizar_productos, name='actualizar_productos'),
    path('actualizar_usuarios/<usuarios_id>', views.actualizar_usuarios, name='actualizar_usuarios'),
]
