from dashboard.models import Products
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cart,Orders,Payment,ConfirmOrder,ShippingAddress


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ['created_at', 'user']
        
    def user_product(self, user):
        return Product.objects.filter(user=user).all()


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
    product = ProductSerializer()
    class Meta:
        model = Cart
        exclude = ['created']
    read_only= True
    
    
    def get_queryset(self):
        return Products.objects.all()
    
    def get_product(self, obj):
        return ProductSerializer(obj.product).data
    
    def get_cart_items(self,user):
        cart = Cart.objects.filter(user = user).all()
        serializer = CartSerializer(cart)
        print(serializer.data)
        return serializer
            
            

class ConfirmOrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = ConfirmOrder
    
    def get_product(self,obj):
        return ProductSerializer(obj.products).data
        
        
            
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
