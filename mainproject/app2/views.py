from django.shortcuts import render



def html(request):
    return render(request,'html.html')

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def MyProfile(request):
    return render(request,'Myprofile.html')

def doahboard(request):
    return render(request,'doahboard.html')

def Shopping(request):
    return render(request,'Shopping.html')

def Teachers(request):
    return render(request,'Teachers.html')

