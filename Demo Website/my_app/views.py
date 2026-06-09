from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from decimal import Decimal
from my_app.forms import *
from my_app.models import *

def home_page(request):
 
    return render(request, 'home.html')

def register_page(request):
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_page')
        
    form_data = RegisterForm()
    context = {
        'form_data':form_data
    }
    return render(request, 'register.html',context)

def login_page(request):
    if request.method == 'POST':
        form_data = LoginForm(request, data=request.POST) 
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            return redirect('dashboard_page')
    
    form_data = LoginForm()
    context = {
        'form_data':form_data
    }
   
    return render(request, 'login.html',context)

@login_required
def logout_page(request):
    logout(request)

    return redirect(login_page)

@login_required
def dashboard_page(request):

    return render(request, 'dashboard.html')

@login_required
def product_list(request):
    user = request.user
    if user.user_type == 'Admin':
        product_data = ProductModel.objects.filter(created_by = user)
    else:
        product_data = ProductModel.objects.all()

    context = {
        'product_data': product_data,
    }

    return render(request, 'product-list.html',context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form_data = ProductForm(request.POST, request.FILES)
        if form_data.is_valid():
            product_data = form_data.save(commit=False)
            product_data.created_by = request.user
            product_data.total = Decimal(product_data.quantity) * Decimal(product_data.price)
            product_data.save()
            return redirect('product_list')
    
    form_data = ProductForm()
    context = {
        'form_data':form_data,
        'title': 'Add Product Info',
        'btn_name': 'Add Product'
    }

    return render(request, 'master/base-form.html', context)

@login_required
def update_product(request, p_id):
    product = ProductModel.objects.get(id=p_id)
    if request.method == 'POST':
        form_data = ProductForm(request.POST, request.FILES, instance=product)
        if form_data.is_valid():
            product_data = form_data.save(commit=False)
            product_data.created_by = request.user
            product_data.total = Decimal(product_data.quantity) * Decimal(product_data.price)
            product_data.save()
            return redirect('product_list')

    form_data = ProductForm(instance =product)
    context = {
        'form_data':form_data,
        'title': 'Update Product Info',
        'btn_name': 'Update Product'
    }
    return render(request, 'master/base-form.html',context)

@login_required
def delete_product(request, p_id):
    ProductModel.objects.get(id=p_id).delete()
    return redirect('product_list')

@login_required
def product_details(request, p_id):
    product = ProductModel.objects.get(id=p_id)
    context = {
        'product_data':product
    }
    return render(request, 'product-details.html', context)
