from django.shortcuts import render
from dashboard.models import Products
from accounts.models import Cart
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
    client = razorpay.Client(auth = ("rzp_live_sLMg1DMpK4cin4", "E5PAeZ5tZZO5XWgcUN9v7FsM"))
    order_amount = 50000
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'
    notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL
    
    try:
        client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='1')
    except Exception as e:
        print(e)
    return render(request, 'buy.html')
    