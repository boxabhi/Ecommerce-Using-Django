from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http.response import JsonResponse
from django.contrib.auth import logout
from .models import Vendor,Cart
from django.contrib.auth import login as auth_login
from dashboard.models import Products
import razorpay

def home(request):
    result = {'success' : 'Everything Fine!'}
    products = Products.objects.all()
   
    context = {'products': products , 'carts' : cart}
    
    return render(request, 'index.html', context)
    
    
def cart(request):
    user = request.user
    if user.id :
        cart = Cart.objects.filter(user = request.user).all()
        context = { 'carts' : cart}
        return render(request, 'cart.html', context)
    return render(request, 'cart.html')
    
    

def buynow(request):
    # client = razorpay.Client(auth = ("rzp_live_sLMg1DMpK4cin4", "E5PAeZ5tZZO5XWgcUN9v7FsM"))
    order_amount = 50000
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'
    notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL
    
    # try:
    #     client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='1')
    # except Exception as e:
    #     print(e)
    return render(request, 'buy.html')
    

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(email = email, username=email)
        user.set_password(password)
        user.save()
        return render(request,'register.html' , {'message' : 'Your account has been created'})
        
    return render(request , 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = email ,password = password)
        if user:
            request.session['email'] = user.email
            request.session['id'] = user.id
            auth_login(request, user)
            return redirect('vendor-info')
        else:
           
            return render(request,'login.html',{'message' : 'Wrong Credentials' }) 
    return render(request , 'login.html')



def vendorinfo(request):
    if request.session.get('id'):
        if Vendor.objects.filter(user =request.session.get('id')):
            return redirect('dashboard-home')
        if request.method == 'POST':
            id = request.session.get('id')
            shop = request.POST.get('shop')
            whatsapp = request.POST.get('whatsapp')
            area = request.POST.get('area')
            pincode = request.POST.get('pincode')
            user = User.objects.get(id = id)
            vendor = Vendor(user = user,shop = shop , whatsapp = whatsapp , area = area , pincode = pincode)
            vendor.save()
            return redirect('dashboard-home')
            
        return render(request , 'info.html')
    else :
        return redirect("404")
    
    
def logout_view(request):
    logout(request)
    return redirect('/')



def add_cart(request, id):
    user = request.user
    if user.id :
        product = Products.objects.get(id=id)
        cart = Cart(user = user , product = product)
        cart.save()
    return redirect('/')

 

def remove(request , id):
   user = request.user
   if not user.is_anonymous:
       cart = Cart.objects.get(id=id , user=user)
       if cart:
           cart.delete()
           return redirect('cart')
       else:
           return redirect('error')
       
       
    


def error(request):
    response = {}
    response['message'] = "You are lost"
    response['status_code'] = 404
    return JsonResponse(response)