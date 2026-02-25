from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def track_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})
