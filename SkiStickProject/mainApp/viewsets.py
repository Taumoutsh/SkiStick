from rest_framework import viewsets
from .models import EstacionToTipoPista
from .models import Estacion, Localizacion, EstacionToUsuario
from .serializers import EstacionSerializer, LocalizacionSerializer, EstacionToUsuarioSerializer

class EstacionViewSet(viewsets.ModelViewSet):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer

class LocalizacionViewSet(viewsets.ModelViewSet):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer

class EstacionToUsuarioViewSet(viewsets.ModelViewSet):
    queryset = EstacionToUsuario.objects.all()
    serializer_class = EstacionToUsuarioSerializer
