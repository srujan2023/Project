
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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
    path('', include('articles.urls')), 
    path('', include('shopping.urls')), 
    
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
      path('karthik/',include('articles.urls')), 
      path('karthik/',include('shopping.urls')),          
               
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


