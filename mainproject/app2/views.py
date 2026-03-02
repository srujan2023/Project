from django.shortcuts import render
from articles.models import articles



def html(request):
    articles_list = articles.objects.order_by('-id')[:5]
    return render(request, 'html.html', {'articles': articles_list})

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def MyProfile(request):
    return render(request,'MyProfile.html')

def doahboard(request):
    return render(request,'doahboard.html')

def Shopping(request):
    return render(request,'Shopping.html')

def Teachers(request):
    return render(request,'Teachers.html')

