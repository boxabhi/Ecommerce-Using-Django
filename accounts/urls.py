from django.urls import path
from .views import register,login,vendorinfo,error,logout_view,add_cart,remove
from dashboard.views import dashboard
urlpatterns = [
    
    path('register' , register , name="register" ),
    path('login' , login , name="login"),
    path('vendor-info' , vendorinfo , name="vendor-info"),
    path('404' , error , name="404"),
    path('dashboard' , dashboard , name="dashboard-home"),
    path('logout' , logout_view , name="logout"),
    
    path('add-cart/<id>' , add_cart , name="add-cart"),
    path('remove/<id>' , remove , name="remove"),
    

]
