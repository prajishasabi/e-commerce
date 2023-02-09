from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'seller/seller_home.html')


def catalog(request):
    return render(request,'seller/product_catalog.html')

def add_product(request):
    return render(request,'seller/add_products.html')

def change_password(request):
    return render(request,'seller/change_password.html')

