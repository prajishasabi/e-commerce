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



def update_stock(request):
    return render(request,'seller/update_stock.html')


def recent_order(request):
    return render(request,'seller/recent_order.html')


def order_history(request):
    return render(request,'seller/order_history.html')


def profile(request):
    return render(request,'seller/profile.html')








