
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .serializers import ProductSerializer , AccountSerializer,CartSerializer
from rest_framework.views import APIView
from .models import Cart,Orders
from dashboard.models import Products
from rest_framework.authtoken.models import Token

from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication

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
        cart = Cart.objects.filter(user = request.user).all()
        serializer = CartSerializer(cart , many=True)
        return Response(serializer.data)
    
    def post(self, request , *args, **kwargs):
        try:
            user = Token.objects.get(token=request.META["HTTP_AUTHORIZATION"].split(" ")[1]).user
        except Token.DoesNotExist:
            return Response({'error' : 'Token not provided'})
        print(request.data)
        serializer = CartSerializer(data = {})
        if serializer.is_valid():
            return Response({'success': 'Saved'})
        else:
            return Response({'eroor': 'Failed'})
   
   
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