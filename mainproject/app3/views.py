from django.shortcuts import render
from django.http import HttpResponse


def app3(request):
    return HttpResponse("This is app3 Output")
