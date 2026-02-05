from django.urls import path
from app2.views import html,About,Contact,MyProfile,doahboard,Shopping,Teachers



urlpatterns = [
      path('app2/',html,name='html'),
      path('app2/About.html',About,name='About.html'),
      path('app2/Shopping.html',Shopping,name='Shopping.html'),
      path('app2/Contact.html',Contact,name='Contact.html'),
      path('app2/Teachers.html',Teachers,name='Teachers.html'),
      path('app2/MyProfile.html',MyProfile,name='MyProfile.html'),
      path('app2/doahboard.html',doahboard,name='doahbord.html'),
      
      
      
      
      
]