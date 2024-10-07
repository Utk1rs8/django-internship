from django.db import models

# Create your models here.
class Bike(models.Model):
        name = models.CharField(max_length=50)
        price = models.IntegerField()
        image=models.ImageField(upload_to="image/")
        engine_capacity = models.TextField(max_length=150)
        mileage = models.TextField(max_length=150)
        transmission = models.TextField(max_length=150)
        weight = models.TextField(max_length=150)
        fuel_tank = models.TextField(max_length=150)
        power = models.TextField(max_length=150)
        tourque = models.TextField(max_length=150)
    

class Register(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField()
        mobile = models.IntegerField()
        password = models.CharField(max_length=25)
        confirmpassword = models.CharField(max_length=25)

class ClientLogin(models.Model):
        name = models.CharField(max_length=50)
        password = models.CharField(max_length=25)

class AdminLogin(models.Model):
        email = models.EmailField()
        password = models.CharField(max_length=25)
        
        class Meta:
                db_table='Rideitadmin'
                verbose_name_plural='Rideitadmin'
                # verbose_name='Student'
                ordering=['email']

class Slider(models.Model):
        image=models.ImageField(upload_to="image/")
        name = models.CharField(max_length=50)
        price = models.IntegerField()