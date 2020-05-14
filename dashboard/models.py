from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
# Create your models here.



class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    price = models.FloatField()
    quanity = models.CharField(max_length=40)
    slug = models.SlugField(max_length= 50 , blank=True)
    discount = models.IntegerField(default=0, blank=True)
    image = models.CharField(max_length= 400)
    description = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.product
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product)
        super(Products, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('product' , kwargs={'slug': self.slug})
    

class Places(models.Model):
    place = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.place
    
    
    