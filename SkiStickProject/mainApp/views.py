from django.shortcuts import render
from .models import Estacion, Localizacion
from django.http import request, response
# Create your views here.

def home(request):
    return render(request, 'index.html')

def estaciones(request):
    estaciones = Estacion.objects.all()
    return render(request, 'estaciones.html', {'estactiones':estaciones})

def estacion(request, id_estacion):
    estacion = Estacion.objects.get(id=id_estacion)
    return render(request, 'estacion.html', {'estacion':estacion})
