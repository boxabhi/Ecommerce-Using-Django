from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    price = models.FloatField()
    quanity = models.CharField(max_length=40)
    discount = models.IntegerField(default=0, blank=True)
    image = models.CharField(max_length= 400)
    
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.product
    
    

class Places(models.Model):
    place = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.place
    
    
    