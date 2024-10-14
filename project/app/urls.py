from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'slider',Sliderviewset)
router.register(r'bikes',Bikesviewset)
router.register(r'register',Registerviewset)
router.register(r'clientlogin',Clientloginviewset)
router.register(r'adminlogin',Adminloginviewset)

urlpatterns = [
    path('', include(router.urls)),
]