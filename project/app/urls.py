
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', Bikesviewset, basename='Bike')
router.register(r'', Registerviewset, basename='Client')
urlpatterns = router.urls