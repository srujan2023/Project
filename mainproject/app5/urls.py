from django.urls import path
from app5.views import app5


urlpatterns = [
      path('app5', app5,name='app5'),
]