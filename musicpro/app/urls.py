from django.urls import path
from .views import home, contacto, galeria, agregar_producto, listar_productos, modificar_producto, eliminar_producto , webpay_plus, webpay_plus_commit, detalle, agregar_car,eliminar_car,restar_producto,limpiar_carro
urlpatterns = [                                                                                                                                                   #carrito                              
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('webpay/<id>/', webpay_plus, name="webpay"),
    path('webpaycommit/', webpay_plus_commit, name="webpay_plus_commit"),
    path('detalle/', detalle, name="detalle"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),

    path('agregar/<int:producto_id>/',agregar_car, name="agregar"), #carrito
    path('eliminar/<int:producto_id>/',eliminar_car, name="eliminar"), #carrito
    path('restar/<int:producto_id>/',restar_producto, name="restar"), #carrito
    path('limpiar/',limpiar_carro, name="limpiar"), #carrito
]
