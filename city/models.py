from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from dashboard.models import Products


# Create your models here.


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
    

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    localty = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    alternate_mobile = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now=True)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    
    def countCart(self):
        return Cart.objects.all().count

    def __str__(self):
        return self.user.username + " has " + self.product.product + " " + str(self.product_id)
    
    
    
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    

class Payment(models.Model):
    razorpay_id = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return seld.user.email    
    
class ConfirmOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipped = models.ForeignKey(ShippingAddress , on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    successfull = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username + " " + self.products.product
    
    
