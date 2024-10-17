from .models import *
from rest_framework import serializers

class BikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bikes
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
        
class ClientloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLogin
        fields = '__all__'

class AdminloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLogin
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'
class AccessoriesItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesItems
        fields = '__all__'