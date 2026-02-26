from django.urls import path
from shopping.views import cart,create_cart,add_to_cart,edit_product,buy_product,payment_success,delete_product

urlpatterns = [
    
     path('cart', cart, name='cart'),
     path('createcart', create_cart, name='create_cart'),
     path('shopping/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
     path('shopping/edit/<int:product_id>/', edit_product, name='edit_product'),
      path('buy/<int:product_id>/', buy_product, name='buy_product'),
    path('payment-success/', payment_success, name='payment_success'),
    path('shopping/delete/<int:product_id>/', delete_product, name='delete_product'),
     
]
