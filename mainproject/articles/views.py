from django.shortcuts import render
from django.http import HttpResponse
from .models import articles as Article


def articles(request):
    articles_list = Article.objects.all()
    return render(request,'html.html',{'articles':articles_list})


def create(request):
    return render(request,'articles.html')

def Create_articles(request): 
    if request.method=='POST':
        title=request.POST.get('title')
        image=request.POST.get('image')
        body=request.POST.get('body')
        author=request.POST.get('author')
       
        stu_obj=Article()
        stu_obj.title=title
        stu_obj.image=image
        stu_obj.body=body
        stu_obj.author=author
        stu_obj.save()
        return render(request,"articles.html")
