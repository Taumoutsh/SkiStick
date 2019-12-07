from rest_framework import routers
from mainApp.viewsets import EstacionViewSet, LocalizacionViewSet, EstacionToTipoPistaViewSet

router = routers.DefaultRouter()
router.register(r'estacion', EstacionViewSet)
router.register(r'localizacion', LocalizacionViewSet)
router.register(r'estaciontotipopista', EstacionToTipoPistaViewSet)