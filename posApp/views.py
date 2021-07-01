  
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from .cart import Cart

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
    print(products)
    context = {'products': products}
    return render(request, 'homeview/products.html', context)


def get_category_page(request):
    categories = Category.objects.all()

    if len(categories) > 0:
        cats = Category.objects.all().order_by("-id")
    args = {'categories': categories, 'cats': cats}
    return render(request, 'homeview/category.html', args)


def get_brand(request):
    brand_obj = Brand.objects.all()

    if len(brand_obj) > 0:
        brands = Brand.objects.all()
    args = {'brands': brands}

    return render(request, 'homeview/brands.html', args)




def get_sell_page(request):
    products = Product.objects.all()
    if len(products) > 0:
        prod_obj = Product.objects.all()
    else:
        prod_obj = None
    
    cart = Cart(request)
    productString = ""

    for item in cart:
        product = item['product']

        b = "{'id':'%s','title':'%s','buying_price':'%s','quantity':'%s', 'total_price':'%s'},"%(product.id, product.title, product.buying_price, item['quantity'], item['total_price'])
        productString = productString + b

    args = {'prod_obj': prod_obj, 'cart': cart, 'productString': productString}
    return render(request, 'homeview/sell.html', args)