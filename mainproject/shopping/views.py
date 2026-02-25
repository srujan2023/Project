from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay
import uuid

from .models import Shopping
from orders.models import Order


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


@login_required
def buy_product(request, product_id):
    product = get_object_or_404(Shopping, id=product_id)

    # Cap the amount to Razorpay's test limit (₹1,00,000)
    max_amount = 100000  # in rupees
    amount_in_paise = min(int(product.Price * 100), max_amount * 100)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    payment = client.order.create({
        "amount": amount_in_paise,  # Razorpay takes amount in paise
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        "product": product,
        "payment": payment,
        "razorpay_key": settings.RAZORPAY_KEY_ID
    }

    return render(request, "payment.html", context)


@login_required
def payment_success(request):
    product_id = request.GET.get("product_id")
    if not product_id:
        return HttpResponse("Payment successful, but product was not provided.")

    product = get_object_or_404(Shopping, id=product_id)
    Order.objects.create(
        user=request.user,
        product_name=product.Productname,
        quantity=1,
        tracking_id=f"TRK-{uuid.uuid4().hex[:10].upper()}",
        status="Processing",
    )
    return redirect("track_orders")


def delete_product(request, product_id):
    product = get_object_or_404(Shopping, id=product_id)
    product.delete()
    return redirect('cart')
