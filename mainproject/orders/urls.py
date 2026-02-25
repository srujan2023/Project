from django.urls import path
from .views import track_orders

urlpatterns = [
    path('track-orders/', track_orders, name='track_orders'),
]