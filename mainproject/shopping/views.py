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
        image = request.FILES.get('image')

        Shopping.objects.create(
            Productname=Productname,
            Price=Price,
            description=description,
            image=image,
        )

        return redirect('cart')

    return render(request, "create_cart.html")


import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Product

def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    payment = client.order.create({
        "amount": int(product.Price * 100),  # Razorpay takes amount in paise
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        "product": product,
        "payment": payment,
        "razorpay_key": settings.RAZORPAY_KEY_ID
    }

    return render(request, "payment.html", context)


from django.http import HttpResponse

def payment_success(request):
    return HttpResponse("Payment Successful 🎉")