from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Teachers


def app1(request):
 teachers = Teachers.objects.all()   
 return render(request,'Teachers.html',{'teachers':teachers})

from django.contrib.auth.models import User

def regsiter(request):   
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        Password=request.POST.get('Password')
        Address=request.POST.get('Address')
        DOB=request.POST.get('DOB')
        Gender=request.POST.get('Gender')
        
        # Create Django User
        user = User.objects.create_user(username=name, password=Password)
        
        stu_obj=Teachers()
        stu_obj.name=name
        stu_obj.age=age
        stu_obj.Password=Password
        stu_obj.Address=Address
        stu_obj.DOB=DOB
        stu_obj.Gender=Gender
        stu_obj.save()
        return redirect('login')  # back to login page
    
    return render(request,'teachers_register.html')

def update(request,id):
    stu_obj=Teachers.objects.get(id=id)
    if request.method=='POST':
        stu_obj.name=request.POST.get('name')
        stu_obj.age=request.POST.get('age')
        stu_obj.Password=request.POST.get('Password')
        
        # stu_obj.enrollment_date=request.POST.get('enrollment_date')
        stu_obj.Address=request.POST.get('Address')
        stu_obj.DOB=request.POST.get('DOB')
        # stu_obj.Teachers_id=request.POST.get('Teachers_id')
        stu_obj.Collage_Name=request.POST.get('Collage_Name')
        stu_obj.Gender=request.POST.get('Gender')
        stu_obj.save()
        return redirect("Teachers.html") 
    return render(request,'update.html',{'teachers':stu_obj})
    


from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('Password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('profile')   # better to use name instead of URL
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Teachers

@login_required
def profile(request):
    try:
        teacher = Teachers.objects.get(name=request.user.username)
    except Teachers.DoesNotExist:
        teacher = None
    return render(request, 'MyProfile.html', {'user': request.user, 'teacher': teacher})