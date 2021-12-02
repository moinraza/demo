from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from employee.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import datetime
import csv



def index(request):
    userd = Superadmin.objects.all().count()
    empd = Employee.objects.all().count()
    return render(request, "index.html", {'userd':userd, 'empd':empd})

def loginpage(request):
    if request.method =="POST": 
        username = request.POST['email']
        password = request.POST['password']
        customer = authenticate(request, username=username, password=password)
        login(request, customer)
        return redirect('Homepage')
    return render(request, "login.html")

def signuppage(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        Email = User.objects.filter(email = email)
        if Email.exists():
            messages.success(request, 'Email is Already Registered')
        u = User.objects.create_user(username=email, first_name=name, email=email, password=password)
        u.is_admin = True
        u.save()
        admin = Superadmin.objects.create(name=name, email = email, password = password, phone = phone, user=u)
        return redirect('LoginPage')
    return render(request, "signup.html")

def userlogout(request):
     if request.user.is_authenticated:
         logout(request)
         return redirect('LoginPage')

def empadd(request):
    if request.method == "POST":
        empid = request.POST['empid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        Email = Employee.objects.filter(email = email)
        if Email.exists():
            messages.error(request, 'Employee is Already Registered')
        elif request.user.is_authenticated:
           emp = Employee.objects.create(id = empid, name=name, email = email, gender = gender, phone = phone)
           messages.success(request, 'Employee is Successfully Added')
        else:
           messages.success(request, 'Please First Login')
           return redirect('LoginPage')    
    return render(request, "addemployeeform.html")

def empview(request):
    empd = Employee.objects.all()
    return render(request, "employeedetail.html",{'empd':empd})

def userview(request):
    userd = Superadmin.objects.all()
    return render(request, "userdetail.html",{'userd':userd})

def empedit(request):
    if request.method == "POST":
        empid = request.POST['empid']
        if request.user.is_authenticated:
           item = Employee.objects.get(id = empid)
        else:
          messages.success(request, 'Please First Login')
          return redirect('LoginPage')
    return render(request, "updateemployee.html" ,{'item':item})

def empupdate(request):
    if request.method == "POST":
        empid = request.POST['empid']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        if request.user.is_authenticated:
           item = Employee.objects.filter(email = email)
           item.update(id = empid, name=name, email = email, gender = gender, phone = phone)
           messages.success(request, 'Employee is Successfully updated')
        else:
          messages.success(request, 'Please First Login')
          return redirect('LoginPage')
    return HttpResponseRedirect(reverse('AllEmployeeDetails'))

def removeemp(request):
    if request.method == "POST":
        empid = request.POST['empid']
        if request.user.is_authenticated:
           item = Employee.objects.get(id = empid)
           item.delete()
        else:
          messages.success(request, 'Please First Login')
          return redirect('LoginPage')
    return HttpResponseRedirect(reverse('AllEmployeeDetails'))

def search(request):
    if request.method == "POST":
        search = request.POST.get('search')
        emps = Employee.objects.filter(Q(id = search))
    return render(request, 'search.html', {'emps':emps})

def export_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=empreport' +\
       str(datetime.datetime.now())+'.csv'
    write = csv.writer(response)
    write.writerow(['Employee ID', 'Employee Name', 'Employee Email', 'Employee Mob.', 'Added Date', 'Gender'])
    emp = Employee.objects.all()
    for i in emp:
        write.writerow([i.id, i.name, i.email, i.phone, i.added_date, i.gender])
    return  response