from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .serializers import ProductSerializer , AccountSerializer,CartSerializer,ConfirmOrderSerializer,ShippingAddressSerializer
from rest_framework.views import APIView
from .models import Cart,Orders,Payment,ConfirmOrder,ShippingAddress
from dashboard.models import Products
from rest_framework.authtoken.models import Token

from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404

class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer


class CartView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self , request):
        cart = Cart.objects.filter(user = 4 , ordered = False).all()
        serializer = CartSerializer(cart , many=True)
        return Response(serializer.data)
    
    def post(self, request , *args, **kwargs):
        product = Products.objects.get(id=request.data['product'])
        cart = Cart(user=request.user, product=product)
        cart.save()
        return Response({'success': 'Added'} , 200)
    
    def delete(self , request):
        user = request.user
        product = request.data['product']
        cart = Cart.objects.filter(user = user , product = product)
        print(cart)
        if cart:
            cart.delete()
            return Response({'success':'removed'} , status=204)
        else:
            return Response({'error' : 'Something went Wrong'})
    
    def put(self, request):
        user = 4
        #product = request.data['product']
        cart = Cart.objects.get(id = request.data['id'])
        print(cart)
        serializer = CartSerializer(instance=cart ,data= {'user' :request.user.id,'quantity' : request.data['quantity']})
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'added'} , status=200)
        else:
            print(serializer.errors)
            return Response({'error' : 'error'})
       

class ProductView(APIView):

    def get(self, request, slug):
        p = get_object_or_404(Products , slug=slug)
        print(p)
        product = Products.objects.get(slug = slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

       

   

class ShippingAddressView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        address = ShippingAddress.objects.filter(user = request.user).first()
        serializer = ShippingAddressSerializer(address)
        return Response(serializer.data)
    
    def post(self , request):
        result = request.data
        result['user'] = request.user.id
        serializer = ShippingAddressSerializer(data = result)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Shipping Address Confirmed'})
        else:
            print(serializer.errors)
            return Response({'error': 'Something went Wrong'})
        
        return Response({'error': 'Something went Wrong'})
          

   
   
@api_view(['GET', 'POST'])
def cart(request):
    if request.method == 'GET':
        token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        cart = CartSerializer()
        email = Token.objects.get(key = token).user
        # cart = Cart.objects.filter(user = email).all()
        # serializers = CartSerializer(cart)
        result = cart.get_cart_items(email)
        return Response(result)
        
        
        
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
  
  
# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     content = {
#         'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#         'auth': unicode(request.auth),  # None
#     }
#     return Response(content)  
    
        
class ExampleView(APIView):

    def get(self, request, format=None):
        content = {
            'user': (request.user),  # `django.contrib.auth.User` instance.
            'auth': (request.auth),  # None
        }
        return Response(content)