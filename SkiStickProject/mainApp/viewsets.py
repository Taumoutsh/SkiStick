from rest_framework import viewsets
from .models import EstacionToTipoPista
from .models import Estacion, Localizacion, EstacionToUsuario
from .serializers import EstacionToTipoPistaSerializer
from .serializers import EstacionSerializer, LocalizacionSerializer, EstacionToTipoPistaSerializer, EstacionToUsuarioSerializer

class EstacionViewSet(viewsets.ModelViewSet):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer

class EstacionToTipoPistaViewSet(viewsets.ModelViewSet):
    queryset = EstacionToTipoPista.objects.all()
    serializer_class = EstacionToTipoPistaSerializer

class LocalizacionViewSet(viewsets.ModelViewSet):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer

class EstacionToUsuarioViewSet(viewsets.ModelViewSet):
    queryset = EstacionToUsuario.objects.all()
    serializer_class = EstacionToUsuarioSerializer
