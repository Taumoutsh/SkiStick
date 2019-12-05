from rest_framework import routers
from mainApp.viewsets import EstacionViewSet

router = routers.DefaultRouter()
router.register(r'estacion', EstacionViewSet)