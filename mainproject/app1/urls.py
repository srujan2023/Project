from django.urls import path
from app1.views import app1,Teachers,update,regsiter,login,profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
       path('profile/', profile, name='MyProfile'),
      path('app2/Teachers.html', app1,name='app1'),
      path('app2/regsiter.html', regsiter,name='regsiter'),
      path('app2/login.html', login,name='login'),
      path('karthik/app2/update/<int:id>/',update,name='update'),
      path('logout/', LogoutView.as_view(), name='logout'),
      
]