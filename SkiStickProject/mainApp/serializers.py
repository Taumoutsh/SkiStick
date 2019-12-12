from rest_framework import serializers
from .models import Estacion, Localizacion, EstacionToUsuario

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacion
        fields = '__all__'

class EstacionToUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstacionToUsuario
        fields = '__all__'