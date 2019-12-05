from rest_framework import serializers
from .models import Estacion
from .models import EstacionToTipoPista

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'

class EstacionToTipoPistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstacionToTipoPista
        fields = '__all__'