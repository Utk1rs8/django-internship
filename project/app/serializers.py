from .models import Bikes
from rest_framework import serializers

class BikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bikes
        fields = '__all__'