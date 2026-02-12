from django.urls import path
from .views import create, article

urlpatterns = [
    path('app2/article/', article, name='article'),
    path('app2/articles/', create, name='create'),
]
