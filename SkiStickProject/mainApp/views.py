from django.shortcuts import render, redirect
from .models import Estacion, Localizacion, TipoPista, EstacionToTipoPista, EstacionToUsuario
from .forms import ComentarioForm, LoginForm, SigninForm
from time import gmtime, strftime
from django.contrib.auth.models import User

def home(request):
    # Le - devant kmsPista signifie descendant, ne rien mettre signifie ascendant
    estacionesPorPistas = Estacion.objects.order_by('-kmsPista')[:3]
    estacionesPorRemontes = Estacion.objects.order_by('-numeroRemontes')[:3]
    estacionesPorAltura = Estacion.objects.order_by('-alturaMaxima')[:3]
    estacionesRandom = Estacion.objects.order_by('?')[:5]

    return render(request, 'index.html', {'estacionesPorPistas':estacionesPorPistas, 'estacionesPorRemontes':estacionesPorRemontes, 'estacionesPorAltura':estacionesPorAltura, 'estacionesRandom': estacionesRandom})

def estaciones(request):
    estaciones = Estacion.objects.all()
    return render(request, 'estaciones.html', {'estactiones':estaciones})

def estacion(request, id_estacion):
    estacion = Estacion.objects.get(id=id_estacion)
    estacionToTipoPista = EstacionToTipoPista.objects.filter(estacion_id=estacion.id)
    estacionToUsuario = EstacionToUsuario.objects.filter(estacion_id=estacion.id)
    form = ComentarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            calificacion = form.cleaned_data['calificacion']
            comentario = form.cleaned_data['comentario']
            showtime = strftime("%d-%m-%Y", gmtime())
            post = EstacionToUsuario.objects.create(calificacion=calificacion, comentario=comentario,
                fecha=showtime, estacion_id=estacion.pk, usuario_id=request.user.id)
            return redirect('/main/estacion/'+id_estacion)
    return render(request, 'estacion.html', {'estacion':estacion, 'estacionToTipoPista':estacionToTipoPista, 'estacionToUsuario':estacionToUsuario, 'form':form})

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

def login(request):
    form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})

def signin(request):
    form = SigninForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['contrasena']
            user = User.objects.create_user(first_name=nombre, last_name=apellido,
                                            username=usuario, email=email, password=contrasena)
            form = SigninForm(None)
    return render(request, 'registration/signin.html', {'form':form})

def gestionEstacion(request):
    return render(request, 'gestionEstacion.html')