from django.http import HttpResponse
from django.shortcuts import render
from .models import Teachers


def app1(request):
 teachers = Teachers.objects.all()
    
 return render(request,'Teachers.html',{'teachers':teachers})
#  return render(request,'html.html');