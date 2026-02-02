from django.shortcuts import render
from django.http import HttpResponse


def app5(request):
    return HttpResponse("This is app5 Output")
