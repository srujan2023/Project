from django.urls import path
from shopping.views import cart,create_cart

urlpatterns = [
    
     path('cart', cart, name='cart'),
     path('createcart', create_cart, name='create_cart'),
     
]