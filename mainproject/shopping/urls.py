from django.urls import path
from shopping.views import cart,create_cart,buy_product,payment_success

urlpatterns = [
    
     path('cart', cart, name='cart'),
     path('createcart', create_cart, name='create_cart'),
      path('buy/<int:product_id>/', buy_product, name='buy_product'),
    path('payment-success/', payment_success, name='payment_success'),
     
]