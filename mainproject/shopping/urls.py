from django.urls import path
from shopping.views import cart

urlpatterns = [
    
     path('cart', cart, name='cart'),
]