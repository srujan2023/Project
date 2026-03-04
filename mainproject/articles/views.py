from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from .models import articles
from django.contrib.auth.decorators import login_required

def _visible_articles_for_user(user):
    if user.is_staff:
        return articles.objects.all()
    return articles.objects.filter(visibility=articles.VISIBILITY_PUBLIC)


def create(request):
    articles_list = _visible_articles_for_user(request.user)
    return render(request, 'articles.html', {'articles': articles_list})


@login_required
def private_articles(request):
    if request.user.is_staff:
        articles_list = articles.objects.filter(visibility=articles.VISIBILITY_PRIVATE)
    else:
        articles_list = articles.objects.filter(
            visibility=articles.VISIBILITY_PRIVATE,
            author=request.user.username,
        )
    return render(request, 'private_articles.html', {'articles': articles_list})


def article_detail(request, id):
    article_obj = get_object_or_404(articles, id=id)
    if (
        article_obj.visibility == articles.VISIBILITY_PRIVATE
        and not request.user.is_staff
        and (not request.user.is_authenticated or request.user.username != article_obj.author)
    ):
        return HttpResponseForbidden("This private article is not accessible.")
    return render(request, 'article_detail.html', {'article': article_obj})


def create_articles(request):
    return render(request, 'create_articles.html',)


def article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        body = request.POST.get('body')
        visibility = request.POST.get('visibility', articles.VISIBILITY_PUBLIC)
        if visibility not in {articles.VISIBILITY_PUBLIC, articles.VISIBILITY_PRIVATE}:
            visibility = articles.VISIBILITY_PUBLIC
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
            author=author,
            visibility=visibility,
        )

        # redirect to the articles list so all users' articles are shown
        return redirect('create')


@login_required
def toggle_like(request, id):
    if request.method != 'POST':
        return redirect('home')

    article_obj = get_object_or_404(articles, id=id)
    if article_obj.likes.filter(id=request.user.id).exists():
        article_obj.likes.remove(request.user)
    else:
        article_obj.likes.add(request.user)
        article_obj.dislikes.remove(request.user)

    is_liked = article_obj.likes.filter(id=request.user.id).exists()
    is_disliked = article_obj.dislikes.filter(id=request.user.id).exists()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({
            "ok": True,
            "liked": is_liked,
            "disliked": is_disliked,
            "likes_count": article_obj.likes.count(),
            "dislikes_count": article_obj.dislikes.count(),
        })

    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER')
    if next_url and url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return redirect(next_url)
    return redirect('home')


@login_required
def toggle_dislike(request, id):
    if request.method != 'POST':
        return redirect('home')

    article_obj = get_object_or_404(articles, id=id)
    if article_obj.dislikes.filter(id=request.user.id).exists():
        article_obj.dislikes.remove(request.user)
    else:
        article_obj.dislikes.add(request.user)
        article_obj.likes.remove(request.user)

    is_liked = article_obj.likes.filter(id=request.user.id).exists()
    is_disliked = article_obj.dislikes.filter(id=request.user.id).exists()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({
            "ok": True,
            "liked": is_liked,
            "disliked": is_disliked,
            "likes_count": article_obj.likes.count(),
            "dislikes_count": article_obj.dislikes.count(),
        })

    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER')
    if next_url and url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return redirect(next_url)
    return redirect('home')
    
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
        visibility = request.POST.get('visibility', articles.VISIBILITY_PUBLIC)
        if visibility in {articles.VISIBILITY_PUBLIC, articles.VISIBILITY_PRIVATE}:
            article_obj.visibility = visibility
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

