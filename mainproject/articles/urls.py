from django.urls import path
from .views import create,article


urlpatterns = [
      path('article', article,name='article'), 
      path('app2/articles.html', create,name='create'), 
      
]