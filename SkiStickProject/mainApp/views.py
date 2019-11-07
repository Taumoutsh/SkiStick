from django.shortcuts import render
from .models import Estacion, Localizacion, TipoPista, EstacionToTipoPista

from pprint import pprint
from django.http import request, response
# Create your views here.

def home(request):
    return render(request, 'index.html')

def estaciones(request):
    estaciones = Estacion.objects.all()
    return render(request, 'estaciones.html', {'estactiones':estaciones})

def estacion(request, id_estacion):
    estacion = Estacion.objects.get(id=id_estacion)
    estacionToTipoPista = EstacionToTipoPista.objects.filter(estacion_id=estacion.id)
    return render(request, 'estacion.html', {'estacion':estacion, 'estacionToTipoPista':estacionToTipoPista})

def localizaciones(request):
    localizaciones = Localizacion.objects.all()
    return render(request, 'localizaciones.html', {'localizaciones':localizaciones})

def localizacion(request, id_localizacion):
    localizacion = Localizacion.objects.get(id=id_localizacion)
    estaciones = Estacion.objects.filter(localizacion_id=id_localizacion)
    return render(request, 'localizacion.html', {'localizacion':localizacion, 'estaciones':estaciones})

def tipospistas(request):
    tipospistas = TipoPista.objects.all()
    return render(request, 'tipospistas.html', {'tipospistas':tipospistas})


def tipopista(request, id_tipoPista):
    tipoPista = TipoPista.objects.get(id=id_tipoPista)
    estacionToTipoPista = EstacionToTipoPista.objects.filter(tipoPista_id=id_tipoPista)
    return render(request, 'tipopista.html', {'tipoPista':tipoPista, 'estacionToTipoPista':estacionToTipoPista})

