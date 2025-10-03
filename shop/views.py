from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"shop/index.html")

def menu(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request,"shop/menu.html",{"catagory":catagory})

def items(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(Catagory__name=name)
        return render(request,"shop/items.html",{"products":products,"cateory":name})
    else:
        messages.warning(request="No Such Chatagory Found")
        return redirect('menu')
    
def login(request):
    return render(request,"shop/login.html")
    
def cart(request):
    return render(request,"shop/cart.html")
 
def about(request):
    return render(request,"shop/about.html")

def review(request):
    return render(request,"shop/review.html")

