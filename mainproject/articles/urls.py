from django.urls import path
from .views import articles,create


urlpatterns = [
      path('app2/articles.html', articles,name='articles'), 
      path('articles.html', create,name='create'), 
      
]