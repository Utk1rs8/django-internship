from .models import *
from rest_framework import serializers

class BikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'