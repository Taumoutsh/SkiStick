from rest_framework import routers
from mainApp.viewsets import EstacionViewSet, LocalizacionViewSet, EstacionToTipoPistaViewSet, EstacionToUsuarioViewSet

router = routers.DefaultRouter()
router.register(r'estacion', EstacionViewSet)
router.register(r'localizacion', LocalizacionViewSet)
router.register(r'estaciontotipopista', EstacionToTipoPistaViewSet)
router.register(r'estaciontousuario', EstacionToUsuarioViewSet)