from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,"core/inicio.html")

def inicio2(request):
    return render(request, "core/inicio2.html")

def autos(request):
    return render(request, "core/autos.html")

def contacto(request):
    return render(request, "core/contacto.html")

def crearcuenta(request):
    return render(request, "core/crearcuenta.html")

def login(request):
    return render(request, "core/login.html")

def motos(request):
    return render(request, "core/motos.html")

def reseñas(request):
    return render(request, "core/reseñas.html")

def reserva(request):
    return render(request, "core/reserva.html")

def ford_mustang(request):
    return render(request, "core/ford_mustang.html")

def volkswagen(request):
    return render(request, "core/volkswagen.html")

def lamboghini(request):
    return render(request, "core/lamboghini.html")

def guerrero(request):
    return render(request, "core/guerrero.html")

def honda(request):
    return render(request, "core/honda.html")

def yamaha(request):
    return render(request, "core/yamaha.html")

def reserva_msj(request):
    mensaje = ""
    if request.method == 'POST':
        mensaje = "¡La reserva se ha realizado con exito!"
    else:
        mensaje="No se pudo realizar la reserva,intente nuevamente"    

    return render(request, 'core/reserva.html', {'mensaje': mensaje})