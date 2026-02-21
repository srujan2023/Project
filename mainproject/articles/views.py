from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import articles
from django.contrib.auth.decorators import login_required

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
        # prefer the logged-in user's username as author
        if request.user.is_authenticated:
            author = request.user.username
        else:
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

        # redirect to the articles list so all users' articles are shown
        return redirect('create')
    
def delete_article(request, id):
    articles_list = get_object_or_404(articles, id=id)
    articles_list.delete()
    articles_list = articles.objects.all()
    return render(request, 'articles.html', {'articles': articles_list})


def logout_view(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required
def profile(request):
    print(request.user)
    return render(request, 'profile.html')

