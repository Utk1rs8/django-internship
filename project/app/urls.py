from django.urls import path
from .views import *
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', Bikesviewset, basename='Bike')
# router.register(r'', Registerviewset, basename='Client')
# router.register(r'', Loginviewset, basename='Login')
# urlpatterns = router.urls
urlpatterns=[
    path("",Bikesviewset,name='Bike'),
    path("Register/",Registerviewset,name='student_list'),
    path('Login/',Loginviewset,name='list')
]