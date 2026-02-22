from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Shopping


def cart(request):
    products = Shopping.objects.all()
    return render(request, "Shopping.html", {"products": products})


def create_cart(request):
    if request.method == 'POST':
        Productname = request.POST.get('Productname')
        Price = request.POST.get('Price')
        description = request.POST.get('description')

        Shopping.objects.create(
            Productname=Productname,
            Price=Price,
            description=description,
        )

        return redirect('cart')

    return render(request, "create_cart.html")