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
    queryset = Bike.objects.all()
    serializer_class = RegisterSerializer