from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
import razorpay
import uuid

from .models import Shopping
from orders.models import Order


def cart(request):
    search_query = request.GET.get("q", "").strip()
    if request.user.is_staff:
        products = Shopping.objects.all()
    else:
        products = Shopping.objects.filter(visibility=Shopping.VISIBILITY_PUBLIC)
    cart_items = request.session.get("cart_items", [])
    cart_item_ids = [int(item_id) for item_id in cart_items]

    if search_query:
        products = products.filter(
            Q(Productname__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    return render(
        request,
        "Shopping.html",
        {
            "products": products,
            "search_query": search_query,
            "cart_item_ids": cart_item_ids,
            "cart_count": len(cart_item_ids),
        },
    )


def create_cart(request):
    if request.method == 'POST':
        Productname = request.POST.get('Productname')
        Price = request.POST.get('Price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        visibility = request.POST.get('visibility', Shopping.VISIBILITY_PUBLIC)
        if visibility not in {Shopping.VISIBILITY_PUBLIC, Shopping.VISIBILITY_PRIVATE}:
            visibility = Shopping.VISIBILITY_PUBLIC

        Shopping.objects.create(
            Productname=Productname,
            Price=Price,
            description=description,
            image=image,
            visibility=visibility,
        )

        return redirect('cart')

    return render(request, "create_cart.html")


@login_required
def private_products(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to view private products.")

    products = Shopping.objects.filter(visibility=Shopping.VISIBILITY_PRIVATE)
    return render(
        request,
        "private_products.html",
        {
            "products": products,
            "cart_count": len(request.session.get("cart_items", [])),
        },
    )


def add_to_cart(request, product_id):
    if request.method != "POST":
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"ok": False, "error": "Method not allowed"}, status=405)
        return redirect("cart")

    get_object_or_404(Shopping, id=product_id)
    cart_items = request.session.get("cart_items", [])
    cart_item_ids = [int(item_id) for item_id in cart_items]
    if product_id not in cart_item_ids:
        cart_item_ids.append(product_id)
        request.session["cart_items"] = cart_item_ids

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"ok": True, "cart_count": len(cart_item_ids), "product_id": product_id})

    return redirect("cart")


def view_cart(request):
    cart_items = request.session.get("cart_items", [])
    cart_item_ids = [int(item_id) for item_id in cart_items]
    cart_products_qs = Shopping.objects.filter(id__in=cart_item_ids)
    product_lookup = {product.id: product for product in cart_products_qs}
    cart_products = [product_lookup[item_id] for item_id in cart_item_ids if item_id in product_lookup]
    total_price = sum((product.Price or 0) for product in cart_products)

    return render(
        request,
        "cart_items.html",
        {
            "cart_products": cart_products,
            "cart_count": len(cart_products),
            "total_price": total_price,
        },
    )


def remove_from_cart(request, product_id):
    if request.method != "POST":
        return redirect("view_cart")

    cart_items = request.session.get("cart_items", [])
    cart_item_ids = [int(item_id) for item_id in cart_items]
    updated_item_ids = [item_id for item_id in cart_item_ids if item_id != product_id]
    request.session["cart_items"] = updated_item_ids
    return redirect("view_cart")


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Shopping, id=product_id)

    if request.method == "POST":
        product.Productname = request.POST.get("Productname")
        product.Price = request.POST.get("Price")
        product.description = request.POST.get("description")
        visibility = request.POST.get("visibility", Shopping.VISIBILITY_PUBLIC)
        if visibility in {Shopping.VISIBILITY_PUBLIC, Shopping.VISIBILITY_PRIVATE}:
            product.visibility = visibility
        image = request.FILES.get("image")
        if image:
            product.image = image
        product.save()
        return redirect("cart")

    return render(request, "edit_cart.html", {"product": product})


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
        product_image=product.image,
        quantity=1,
        tracking_id=f"TRK-{uuid.uuid4().hex[:10].upper()}",
        status="Processing",
    )
    return redirect("track_orders")


@login_required
def delete_product(request, product_id):
    if request.method != "POST":
        return redirect("cart")

    product = get_object_or_404(Shopping, id=product_id)
    product.delete()
    return redirect("cart")
