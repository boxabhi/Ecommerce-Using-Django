from django.urls import path

from .views import (
                    register,login,vendorinfo,error,logout_view,
                    add_cart,remove,home,cart,buynow,order_confirmed,
                    )

from dashboard.views import dashboard

from .api import ProductList, UserList, ExampleView, CartView,ShippingAddressView,ProductView

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [    
    path('' , home , name="home"),
    path('cart', cart , name="cart"),
    path('buynow',buynow , name="buynow"),
    
     path('register' , register , name="register" ),
    path('login' , login , name="login"),
    path('vendor-info' , vendorinfo , name="vendor-info"),
    path('404' , error , name="404"),
    path('dashboard' , dashboard , name="dashboard-home"),
    path('logout' , logout_view , name="logout"),
    
    path('add-cart/<id>' , add_cart , name="add-cart"),
    path('remove/<id>' , remove , name="remove"),
    
    path('order-confirmed/<id>' , order_confirmed , name="order-confirmed"),
    
    path('api/' , ProductList.as_view() , name="ProductList"),
    path('api/users' ,UserList.as_view()  , name="User"),
    path('api/cart' ,CartView.as_view() , name="cart"),
    path('api/auth', ExampleView.as_view() , name="auth"),
    path('api/shipping' , ShippingAddressView.as_view() , name="shipping"),
    path('api/token', obtain_auth_token, name='api_token_auth'),
    path('api/product/<slug>' , ProductView.as_view() , name="product")

]
