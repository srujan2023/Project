from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from shopping.models import Shopping

@login_required
def track_orders(request):
    orders = Order.objects.filter(user=request.user)
    missing_image_names = [
        order.product_name for order in orders if not order.product_image
    ]

    fallback_images = {}
    if missing_image_names:
        products = (
            Shopping.objects.filter(Productname__in=missing_image_names)
            .exclude(image="")
            .exclude(image__isnull=True)
            .order_by("-id")
        )
        for product in products:
            if product.Productname not in fallback_images:
                fallback_images[product.Productname] = product.image.url

    for order in orders:
        if order.product_image:
            order.display_image_url = order.product_image.url
        else:
            order.display_image_url = fallback_images.get(order.product_name)

    return render(request, 'orders.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.product_image:
        order.display_image_url = order.product_image.url
    else:
        fallback_product = (
            Shopping.objects.filter(Productname=order.product_name)
            .exclude(image="")
            .exclude(image__isnull=True)
            .order_by("-id")
            .first()
        )
        order.display_image_url = fallback_product.image.url if fallback_product else None

    return render(request, 'order_detail.html', {'order': order})


@login_required
def live_order_status(request):
    orders = Order.objects.filter(user=request.user).values("id", "status")
    return JsonResponse({"orders": list(orders)})
