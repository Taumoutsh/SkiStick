from rest_framework import viewsets
from .models import EstacionToTipoPista
from .models import Estacion
from .serializers import EstacionToTipoPistaSerializer
from .serializers import EstacionSerializer

class EstacionViewSet(viewsets.ModelViewSet):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
    querysetEstacionToTipoPista = EstacionToTipoPista.objects.all()
    serializer_class_EstacionToTipoPista = EstacionToTipoPistaSerializer
