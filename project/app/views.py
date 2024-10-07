from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
import io

# Create your views here.
class Bikesviewset(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikesSerializer

class Registerviewset(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class Loginviewset(viewsets.ModelViewSet):
    queryset = ClientLogin.objects.all()
    serializer_class = LoginSerializer

class Sliderviewset(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
