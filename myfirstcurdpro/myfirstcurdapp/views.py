from django.shortcuts import render,redirect
from .models import Employee
from .forms import CreateForm,updateform,Deleteform
from django.http import HttpResponse


def create_view(request):
    if request.method=="POST":
        cform=CreateForm(request.POST)
        if cform.is_valid():
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            user_name=request.POST.get('user_name')
            password=request.POST.get('password')
            mobile=request.POST.get('mobile')
            date=Employee(first_name=first_name,
                          last_name=last_name,
                          email=email,
                          user_name=user_name,
                          password=password,
                          mobile=mobile
                          )
            date.save()
            cform = CreateForm()
            return render(request, 'register.html', {'cform': cform})
        else:
            return HttpResponse('form is not valid')
    else:
        cform=CreateForm()
        return render(request,'register.html',{'cform':cform})
def Show(request):
    employee=Employee.objects.all()
    return render(request,'show.html',{'employee':employee})
def update(request):
    if request.method=="POST":
        uform=updateform(request.POST)
        if uform.is_valid():
            employees=Employee.objects.get(id=id)
            uform=updateform(request.POST,instance=employees)
            if uform.is_valid():
                uform.save()
                return redirect("/show")
            else:
                return HttpResponse('both data is same')
        else:
           uform=updateform()
           return render(request,'update.html',{'uform':uform})


def delete(request):
    return None