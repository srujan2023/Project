from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from .models import Shopping


def cart(request):
    return render(request,"Shopping.html")

def create_cart(request):
    if request.method=='POST':
        Productname=request.POST.get('Productname')
        Price=request.POST.get('Price')
        description=request.POST.get('description')
        
        stu_obj=Shopping()
        stu_obj.Productname=Productname
        stu_obj.Price=Price
        stu_obj.description=description
        stu_obj.save()
        
        print(Productname,Price,description)
        return HttpResponse("Cart created successfully")        

    return render(request,"create_cart.html")