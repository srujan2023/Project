from django.shortcuts import render
from django.http import HttpResponse
from .models import articles


def create(request):
    return render(request,'articles.html')


def article(request): 
    if request.method=='POST':
        title=request.POST.get('title')
        image=request.POST.get('image')
        body=request.POST.get('body')
        author=request.POST.get('author')
        
        print('title:',title)
        print('image:',image)
        print('body:',body)
        print('author:',author)
        
        
        stu_obj=articles()
        stu_obj.title=title
        stu_obj.image=image
        stu_obj.body=body
        stu_obj.author=author
        stu_obj.save()
    return render(request,'articles.html')
        
      