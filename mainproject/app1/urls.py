from django.urls import path
from app1.views import app1,Teachers,update,regsiter,login


urlpatterns = [
      path('app2/Teachers.html', app1,name='app1'),
      path('app2/regsiter.html', regsiter,name='regsiter'),
      path('app2/login.html', login,name='login'),
      path('karthik/app2/update/<int:id>/',update,name='update')
      
]