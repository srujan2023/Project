from django.urls import path
from .views import track_orders, order_detail, live_order_status

urlpatterns = [
    path('track-orders/', track_orders, name='track_orders'),
    path('track-orders/<int:order_id>/', order_detail, name='order_detail'),
    path('track-orders/live-status/', live_order_status, name='live_order_status'),
]
