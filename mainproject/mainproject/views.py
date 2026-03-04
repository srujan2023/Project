from django.http import HttpResponse
from django.shortcuts import render
from articles.models import articles
from shopping.models import Shopping

def home(request):
    if request.user.is_staff:
        visible_articles = articles.objects.all()
    else:
        visible_articles = articles.objects.filter(visibility=articles.VISIBILITY_PUBLIC)

    articles_list = visible_articles.order_by('-id')[:5]  # Get latest 5 visible articles
    products = Shopping.objects.all()[:6]  # Get latest 6 products
    liked_article_ids = []
    disliked_article_ids = []
    if request.user.is_authenticated:
        liked_article_ids = list(request.user.liked_articles.values_list('id', flat=True))
        disliked_article_ids = list(request.user.disliked_articles.values_list('id', flat=True))
    return render(request, 'html.html', {
        'articles': articles_list,
        'products': products,
        'liked_article_ids': liked_article_ids,
        'disliked_article_ids': disliked_article_ids,
    })

def contact(request):
    return HttpResponse("7975478551")

def email(request):
    return HttpResponse("srujan2004ab@gmial.com")


def dashbord(request):
    return HttpResponse("Welcome to Dashbord")

def skills(request):
    return HttpResponse("Skills Like HTML,CSS,JS,PHP,NODEJS")

def myprofile(request):
    return HttpResponse("Welcome to profile Page")



def shopping_page(request):
    return HttpResponse("Welcome to Shopping Page")

def Myorders(request):
    return HttpResponse("Tracking Your orders")

def feedback(request):
    return HttpResponse("Feedback Page")

