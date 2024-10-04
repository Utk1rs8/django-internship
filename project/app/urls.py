from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',Bikesviewset, basename='user')
urlpatterns = router.urls