from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import articles

def create(request):
    articles_list = articles.objects.all()
    return render(request, 'articles.html', {'articles': articles_list})

def create_articles(request):
    return render(request, 'create_articles.html',)

    

   

def article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        body = request.POST.get('body')
        author = request.POST.get('author')
        
        print("Title:", title)
        print("Image:", image)  
        print("Body:", body)
        print("Author:", author)

        articles.objects.create(
            title=title,
            image=image,
            body=body,
            author=author
        )
        
        return render(request, 'articles.html', {'success': True})
    
def delete_article(request, id):
    articles_list = get_object_or_404(articles, id=id)
    articles_list.delete()
    articles_list = articles.objects.all()
    return render(request, 'articles.html', {'articles': articles_list})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'profile.html')



