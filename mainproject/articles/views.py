from django.shortcuts import render,redirect
from .models import articles

def create(request):
    articles = articles.objects.all()
    return render(request, 'articles.html', {'articles': articles})



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
       
    return render(request, 'articles.html')
    # return redirect("app2/")