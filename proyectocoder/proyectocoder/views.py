from django.http import HttpResponse

from datetime import datetime

from django.template import Template, Context, loader


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
    #abrimos el archivo
    archivo = open(r"C:\Users\Eddy\Desktop\proyectocoder\proyectocoder\proyectocoder\templates\appcoder\plantilla.html")
    #creamos el objeto "plantilla"
    plantilla = Template(archivo.read())
    #cerranis ek archivo para liberar recursos
    archivo.close()
    
    #diccionario con datos para la platilla
    datos = {"nombre": "Edgar","fecha": datetime.now(),"apellido":"Espinola","edad":29} 
    #creamos el contexto
    contexto = Context(datos)
    #renderizamos la plantilla para crear respuesta
    documento = plantilla.render(contexto)
    #retornamos respuesta
    return HttpResponse(documento)

def vista_listado_alumnos(request):
    #abrimos el archivo
    archivo = open(r"C:\Users\Eddy\Desktop\proyectocoder\proyectocoder\proyectocoder\templates\appcoder\listado_alumnos.html")

    #creamos el template
    plantilla = Template(archivo.read())
        
    #cerramos el archivo
    archivo.close()

    #creamos el diccionario de datos
    listado_alumnos = ["edgar espinola","martin garcia","angelo pattina","diego ibarra","federico Gomez"]
    
    datos = {"tecnologia":"python","listado_alumnos":listado_alumnos}

    #creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

# segunda forma de templates ahorrando codigos import loader
def vista_listado_alumnos2(request):
    listado_alumnos = ["edgar espinola","martin garcia","angelo pattina","diego ibarra","federico Gomez"]
    
    datos = {"tecnologia":"python","listado_alumnos":listado_alumnos}

    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)

def lista_familia(request):
    lista_familia = ["Maria Espinola,Eduardo Espinola,Edgar Espinola"]
    
    datos = {"desafio":"familia","lista_familia":lista_familia}

    plantilla = loader.get_template("listado_familia.html")
    
    documento = plantilla.render(datos)

    return HttpResponse(documento)
    