from django.http import HttpResponse
from django.shortcuts import render
from articles.models import articles
from shopping.models import Shopping

def home(request):
    articles_list = articles.objects.all()[:5]  # Get latest 5 articles
    products = Shopping.objects.all()[:6]  # Get latest 6 products
    return render(request, 'html.html', {'articles': articles_list, 'products': products})

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

