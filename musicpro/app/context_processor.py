from app.carro import Carro


def importe_carro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total+(int(value["precio"])*value["cantidad"])
    return {"importe_carro": total}