from django.http import HttpResponse

def home(request):
    return HttpResponse("Hii This is my project")

def contact(request):
    return HttpResponse("7975478551")

def email(request):
    return HttpResponse("srujan2004ab@gmial.com")


def dashbord(request):
    return HttpResponse("Welcome to Dashbord")

def skills(request):
    return HttpResponse("Skills Like HTML,CSS,JS,PHP,NODEJS")

def myprofile(request):
    return HttpResponse("Welcome to profile Page")



def Shopping(request):
    return HttpResponse("Welcome to Shopping Page")

def Myorders(request):
    return HttpResponse("Tracking Your orders")

def feedback(request):
    return HttpResponse("Feedback Page")

