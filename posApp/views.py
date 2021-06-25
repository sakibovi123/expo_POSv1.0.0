  
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def get_home_page(request):
    if 'qry' in request.GET:
        qry = request.GET['qry']
        emps = Employee.objects.filter(emp_id__icontains=qry)
        
    else:
        emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'homeview/base.html', context)

def get_emp_details(request, id):
    emp_details = Employee.objects.get(pk=id)
    context = {'emp_details': emp_details}
    
    return render(request, 'homeview/employee_details.html', context)


def get_employee_search(request):
    if request.method == 'GET':
        qry = request.GET['qry']
        emps = Employee.objects.filter(emp_id__icontains=qry)
        context = {'emps': emps}
        
        return render(request, 'homeview/base.html', context)
        

def admin_login(request):
    if request.method == 'POST':    
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            
            return redirect('base')
    return render(request, 'homeview/login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')



def get_products_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'homeview/products.html', context)
