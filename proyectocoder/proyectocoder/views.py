from django.http import HttpResponse

from datetime import datetime

from django.template import Template, Context


def vista_saludo(request):
    return HttpResponse(" <h1> hola coders! <h1/> ")

def iniciar_sesion(request):
    return HttpResponse("Pasame tu username y tu password por WhatsApp")

def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"hoy es {hoy} - bienvenido {nombre}" 
    return HttpResponse (respuesta)

def anio_nacimiento(request,edad):
    
    edad = int(edad)

    anio_nac = datetime.now().year - edad
    return HttpResponse (f"naciste en {anio_nac}")

def vista_plantilla(request):
    archivo = open("C:\Users\Eddy\Desktop\proyectocoder\proyectocoder\proyectocoder\templates\plantilla.html")

    plantilla = Template(archivo.read())

    archivo.close()

    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)