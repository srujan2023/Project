from django.urls import path
from app2.views import uuu


urlpatterns = [
      path('app2', uuu,name='uuu'),
]