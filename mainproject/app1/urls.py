from django.urls import path
from app1.views import app1,Teachers


urlpatterns = [
      path('app2/Teachers.html', app1,name='app1'),
      
]