from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Teachers


def app1(request):
 teachers = Teachers.objects.all()
    
 return render(request,'Teachers.html',{'teachers':teachers})

def regsiter(request):   
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        Password=request.POST.get('Password')
        # enrollment_date=request.POST.get('enrollment_date')
        Address=request.POST.get('Address')
        DOB=request.POST.get('DOB')
        # Teachers_id=request.POST.get('Teachers_id')
        # Collage_name=request.POST.get('Collage_name')
        Gender=request.POST.get('Gender')
        
        stu_obj=Teachers()
        stu_obj.name=name
        stu_obj.age=age
        stu_obj.Password=Password
        # stu_obj.enrollment_date=enrollment_date
        stu_obj.Address=Address
        stu_obj.DOB=DOB
        # stu_obj.Teachers_id=Teachers_id
        # stu_obj.Collage_Name=Collage_name
        stu_obj.Gender=Gender
        stu_obj.save()
        #print("Teacher_name":,name)
        # print("Student Name:",name)
        # print("age:",age)
        # print("enrollment_date:",enrollment_date)
        # print("address:",address)
        # print("DOB:",DOB)
        # print("callagename",callagename)
        # print("id:",id)
        # print("gender:",gender)   
        return redirect("/") 
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
    
