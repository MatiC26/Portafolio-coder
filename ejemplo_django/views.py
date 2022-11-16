from django.template import Template
from django import Context
from http import HttpResponse

def lista_alumnos(request):
    
    archivo = open("ejemplo_django\ejemplo_django\templates")
    plantilla = Template(archivo.read())
    
    archivo.close()
    
    listado_alumnos = ["Matias Carignano", "Tomas Pandullo", "Juan Buongiorno"]
    
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos }
    
    contexto = Context(datos) 
    
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)
    