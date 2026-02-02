"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home
from .views import contact
from .views import email
from .views import email
from .views import dashbord
from .views import  Shopping
from .views import  Myorders
from .views import feedback
from .views import myprofile
from .views import skills

urlpatterns = [
    path('admin/', admin.site.urls),
      path('', home,name='home'),
      
      path('contact',contact,name='contact'),
      
      path('skills', skills,name='skills'),
      path('email', email,name='email'),
      path('dashbord', dashbord,name='dashbord'),
      path('shopping', Shopping,name='shopping'),
      path('Myorders', Myorders,name='Myorders'),
      path('feedback', feedback,name='feedback'),
      path('myprofile', myprofile,name='myprofile'),
      path('karthik/',include('app1.urls')),
      path('karthik/',include('app2.urls')),
      path('karthik/',include('app3.urls')),
      path('karthik/',include('app4.urls')),
      path('karthik/',include('app5.urls')),
      
      
      
]
