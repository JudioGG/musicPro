from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
from transbank.error.transbank_error import TransbankError

import random
from transbank.webpay.webpay_plus.transaction import Transaction
from .carro import Carro  #Carrito
from django.shortcuts import redirect #Carrito
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"

        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')


def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else: 
           data["form"] = formulario     

    return render(request, 'app/producto/agregar.html', data)

def detalle(request):
    return render(request, 'app/detalle.html')    

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario    
    return render(request, 'app/producto/modificar.html', data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")

#webpay


def webpay_plus(request, id):
    print("Webpay plus create transaction")
    prod = Producto.objects.get(id = id)
    #precio = request.POST.get("precio")
    buy_order = str(random.randrange(100000, 999999))
    session_id = str(random.randrange(100000, 999999))
    amount = prod.precio
    return_url = 'http://127.0.0.1:8000/webpaycommit/'

    response = Transaction.create(buy_order,session_id,amount, return_url)

    print(response)

    data = {
        'response' : response
    }

    return render(request, 'webpay\create.html', data)

def webpay_plus_carrito(request, monto):
    print("Webpay plus carrito create transaction")
    #prod = Producto.objects.get(id = id)
    #precio = request.POST.get("precio")
    buy_order = str(random.randrange(100000, 999999))
    session_id = str(random.randrange(100000, 999999))
    amount = monto #prod.precio
    return_url = 'http://127.0.0.1:8000/webpaycommit/'

    response = Transaction.create(buy_order,session_id,amount, return_url)

    print(response)

    data = {
        'response' : response
    }

    return render(request, 'webpay\create.html', data)

def webpay_plus_commit(request):
    token = request.POST.get("token_ws")
    print("commit for token_ws: {}".format(token))

    response = Transaction.commit(token=token)
    print("response: {}".format(response))

    data = {
        'token' : token,
        'response' : response
    }
    return render(request, 'webpay\commit.html', data)

def webpay_plus_refund(request):
    token = request.POST.get("token_ws")
    amount = request.POST.get("amount")
    print("refund for token_ws: {} by amount: {}".format(token, amount))

    try:
        response = Transaction.refund(token, amount)
        print("response: {}".format(response))

        data = {
            'token' : token,
            'amount' : amount,
            'response' : response
        }
        return render(request, 'webpay\refund.html',data)
    except TransbankError as e:
        print(e.message)



#----------CARRITO------
def agregar_car(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("home")

def eliminar_car(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("home")

def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("home")

def limpiar_carro(request, producto_id):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("home")