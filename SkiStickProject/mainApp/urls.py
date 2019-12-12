from django.contrib import admin
from django.urls import path, include
from mainApp.routers import router
from mainApp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('estaciones', views.estaciones, name='estaciones'),
    path('estacion/<id_estacion>', views.estacion, name='estacion'),
    path('localizaciones', views.localizaciones, name='localizaciones'),
    path('localizacion/<id_localizacion>', views.localizacion, name='localizacion'),
    path('tipospistas', views.tipospistas, name='tipospistas'),
    path('tipopista/<id_tipoPista>', views.tipopista, name='tipopista'),
    path('cuento/', include('django.contrib.auth.urls')),
    path('cuento/signin/', views.signin, name='signin'),
    path('admin/estaciones/',views.gestionEstacion, name='gestionEstacion'),
    path('api/', include(router.urls)),
]