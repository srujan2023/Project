from django.urls import path
from .views import create, article, create_articles, delete_article, edit_article, logout_view, profile, article_detail


urlpatterns = [
     path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('app2/article/', article, name='article'),
    path('app2/articles/', create, name='create'),
    path('app2/articles/<int:id>/', article_detail, name='article_detail'),
    path('app2/create_articles', create_articles, name='create_artilces'),
    path('edit/<int:id>/', edit_article, name='edit_article'),
    path('delete/<int:id>/', delete_article, name='delete_article'),
    
]
