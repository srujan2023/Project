from django.urls import path
from app2.views import html



urlpatterns = [
      path('app2',html,name='html'),
      
]