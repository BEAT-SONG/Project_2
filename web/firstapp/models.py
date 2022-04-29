from django.db import models

# Create your models here.
  
class Car(models.Model):
    brand = models.CharField(max_length = 255,default = '')
    model = models.CharField(max_length = 255,default = '')
    year = models.IntegerField(default = '')
    price = models.IntegerField(default = '')
    transmission = models.CharField(max_length = 255,default = '')
    mileage = models.IntegerField(default = '')
    fuelType = models.CharField(max_length = 255,default = '')
    mpg = models.FloatField(default = '')
    engineSize = models.FloatField(default = '')
    
    def __str__(self):
        return self.brand
