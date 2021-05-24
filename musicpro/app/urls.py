from django.urls import path
from .views import home, contacto, galeria, agregar_producto, listar_productos, modificar_producto, eliminar_producto , webpay_plus, webpay_plus_commit, detalle
urlpatterns = [
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
]
