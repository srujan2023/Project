from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
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
    
@login_required
def delete_article(request, id):
    if request.method != 'POST':
        return redirect('create')

    article_obj = get_object_or_404(articles, id=id)
    can_delete = request.user.is_staff or request.user.username == article_obj.author
    if not can_delete:
        return HttpResponseForbidden("You are not allowed to delete this article.")

    article_obj.delete()
    return redirect('create')


@login_required
def edit_article(request, id):
    article_obj = get_object_or_404(articles, id=id)
    can_edit = request.user.is_staff or request.user.username == article_obj.author
    if not can_edit:
        return HttpResponseForbidden("You are not allowed to edit this article.")

    if request.method == 'POST':
        article_obj.title = request.POST.get('title')
        article_obj.body = request.POST.get('body')
        new_image = request.FILES.get('image')
        if new_image:
            article_obj.image = new_image
        article_obj.save()
        return redirect('create')

    return render(request, 'edit_article.html', {'article': article_obj})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    print(request.user)
    return render(request, 'profile.html')

