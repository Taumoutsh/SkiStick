from django.contrib import admin
from django.urls import path, include
from mainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estaciones', views.estaciones, name='estaciones'),
    path('estacion/<id_estacion>', views.estacion, name='estacion')
]