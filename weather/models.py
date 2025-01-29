from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

"""
UZ: User uchun model yaratish:
EN: Creating a model for the user:
"""
class CustomUser(AbstractUser):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)

    def __str__(self):
        return self.surname
    
"""
UZ: Ranglar uchun model yaratish:
EN: Create a model for colors:  
"""
class TemperatureColor(models.Model):
    temperature = models.CharField(max_length=50)
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    color_name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.min_temp}°C - {self.max_temp}°C: {self.color_name} ({self.hex_code})"

class WindColor(models.Model):
    wind_speed = models.CharField(max_length=50)
    min_wind = models.FloatField()
    max_wind = models.FloatField()
    color_name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.min_wind} km/h - {self.max_wind} km/h: {self.color_name} ({self.hex_code})"

class CloudColor(models.Model):
    cloud_coverage = models.CharField(max_length=50)
    min_cloud = models.FloatField()
    max_cloud = models.FloatField()
    color_name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.min_cloud}% - {self.max_cloud}%: {self.color_name} ({self.hex_code})"
