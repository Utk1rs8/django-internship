from .models import Bike
from rest_framework import serializers

class BikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'