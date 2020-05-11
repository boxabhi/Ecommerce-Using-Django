from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from dashboard.models import Products


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=500, blank=True)
    area = models.CharField(max_length=30, blank=True)
    pincode = models.CharField(max_length=10)
    
    token = models.CharField(max_length=500, blank=True)
    isverified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.mobile



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return self.user.email
   
    
    
    