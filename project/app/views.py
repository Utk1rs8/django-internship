from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import io

# Create your views here.
class Bikesviewset(viewsets.ModelViewSet):
    queryset = Bikes.objects.all()
    serializer_class = BikesSerializer

class Registerviewset(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class Clientloginviewset(viewsets.ModelViewSet):
    queryset = ClientLogin.objects.all()
    serializer_class = ClientloginSerializer

class Adminloginviewset(viewsets.ModelViewSet):
    queryset = AdminLogin.objects.all()
    serializer_class = AdminloginSerializer

class Sliderviewset(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class AccessoriesItemsviewset(viewsets.ModelViewSet):
    queryset = AccessoriesItems.objects.all()
    serializer_class = AccessoriesItemsSerializer
