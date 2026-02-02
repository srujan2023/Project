from django.shortcuts import render
from django.http import HttpResponse


def app1(request):
    return HttpResponse("This is app1 Output")
