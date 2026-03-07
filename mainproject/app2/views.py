from django.shortcuts import render
from articles.models import articles
from app1.models import Teachers as TeacherModel



def html(request):
    articles_list = articles.objects.order_by('-id')
    liked_article_ids = []
    disliked_article_ids = []
    if request.user.is_authenticated:
        liked_article_ids = list(request.user.liked_articles.values_list('id', flat=True))
        disliked_article_ids = list(request.user.disliked_articles.values_list('id', flat=True))
    return render(request, 'html.html', {
        'articles': articles_list,
        'liked_article_ids': liked_article_ids,
        'disliked_article_ids': disliked_article_ids,
    })

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def MyProfile(request):
    teacher = None
    if request.user.is_authenticated:
        teacher = TeacherModel.objects.filter(name=request.user.username).first()

    return render(request, 'MyProfile.html', {'teacher': teacher})

def doahboard(request):
    return render(request,'doahboard.html')

def Shopping(request):
    return render(request,'Shopping.html')

def Teachers(request):
    return render(request,'Teachers.html')
