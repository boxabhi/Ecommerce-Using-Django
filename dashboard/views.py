from django.shortcuts import render
from .models import Products
# Create your views here.




def dashboard(request):
    products = Products.objects.filter(user = request.user).all()
    print(request.user)
    context = {'products': products}
    if request.method == "POST":
        product = request.POST.get('product')
        price = request.POST.get('price')
        quanity = request.POST.get('quanity')
        discount = request.POST.get('discount')
        image = request.POST.get('image')
        product = Products(user = request.user,product=product , price=price, quanity=quanity ,discount=discount,image=image)
        product.save()
        products = Products.objects.filter(user = request.user).all()
        context = {'message': "Product added" , 'products': products}
        return render(request , 'dashboard.html',context)
    
    return render(request , 'dashboard.html' , context)



def createproducts(request):
    return render(request , 'products.html')