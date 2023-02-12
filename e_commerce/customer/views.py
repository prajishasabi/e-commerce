from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'customer/home.html')


def my_cart(request):
    return render(request,'customer/my_cart.html')


def my_order(request):
    return render(request,'customer/my_order.html')


def change_password(request):
    return render(request,'customer/change_password.html')


def products(request):
    return render(request,'customer/products.html')


def profile(request):
    return render(request,'customer/profile.html')


def logout(request):
    return render(request,'customer/logout.html')



