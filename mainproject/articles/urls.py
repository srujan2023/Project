from django.urls import path
from .views import create, article,create_articles,delete_article,profile


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('app2/article/', article, name='article'),
    path('app2/articles/', create, name='create'),
    path('app2/create_articles', create_articles, name='create_artilces'),
    path('delete/<int:id>/', delete_article, name='delete_article'),
    
]
