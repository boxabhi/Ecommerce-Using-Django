from dashboard.models import Products
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cart,Orders


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ['created_at']
        
        
        


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        def create(self,validate_data):
            user = User(email = validate_data['email'] , username = validate_data['username'])
            user.set_password(validate_data['password'])
            user.save()
            return user
    
    

class CartSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        exclude = ['created']
        
    def get_product(self, obj):
        return ProductSerializer(obj.product).data
    
    def get_cart_items(self,user):
        cart = Cart.objects.filter(user = user).all()
        serializer = CartSerializer(cart)
        print(serializer.data)
        return serializer
            

            
            
        
    
