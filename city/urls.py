from django.urls import path
from .views import home,cart,buynow



urlpatterns = [    
    path('' , home , name="home"),
    path('cart', cart , name="cart"),
    path('buynow',buynow , name="buynow")

]
