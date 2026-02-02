from django.urls import path
from app1.views import app1


urlpatterns = [
      path('', app1,name='app1'),
]