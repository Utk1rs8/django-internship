from django.db import models

# Create your models here.
class Bike(models.Model):
        name = models.CharField(max_length=50)
        price = models.IntegerField()
        image=models.ImageField(upload_to="image/")
        engine_capacity = models.TextField(max_length=150)
        malage = models.TextField(max_length=150)
        transmission = models.TextField(max_length=150)
        weight = models.TextField(max_length=150)
        fuel_tank = models.TextField(max_length=150)
        power = models.TextField(max_length=150)
        tourque = models.TextField(max_length=150)
    
