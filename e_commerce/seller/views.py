
from django.shortcuts import render,redirect
from common.models import Seller
from  .models import Product
from .decorators import auth_seller



# Create your views here.

def home(request):
    # seller = Seller.objects.get(id = request.session['seller'])
    seller = Seller.objects.filter(id = request.session['seller']).values('seller_name','pic')
    seller_name = seller[0]['seller_name']
    seller_pic = seller[0]['pic']
    print(seller_pic)
    return render(request,'seller/seller_home.html',{'name':seller_name,'pic': seller_pic})

@auth_seller

def catalog(request):
    products = Product.objects.filter(seller = request.session['seller'])

    return render(request,'seller/product_catalog.html',{'products':products})

@auth_seller

def add_product(request):
    msg  = ''
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_code = request.POST['product_code']
        description = request.POST['description']
        stock = request.POST['stock']
        price = request.POST['price']
        image = request.FILES['image']

        product_exist = Product.objects.filter(code = product_code,seller = request.session['seller']).exists()

        if not product_exist:
            product = Product(product_name = product_name,code = product_code,description = description, stock = stock, 
                            price = price,pic = image, seller_id = request.session['seller'])
            product.save()

        else:
            msg = 'product code already added'


        

       

    return render(request,'seller/add_products.html',{'message':msg})

@auth_seller
def change_password(request):
    error_msg = ''
    success_msg = '' 
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if len(new_password) >= 8:
                seller = Seller.objects.get(id = request.session['seller'])
                if seller.password == old_password:
                    seller.password = new_password
                    seller.save()
                    success_msg = 'Password changed successfully'
                else:
                    error_msg = 'Incorrect password'

            else:
                error_msg = 'Password should be 8 characters long'
        else:
            error_msg = 'Password doesn\'t match'

    
            



    return render(request,'seller/change_password.html',{'error_msg':error_msg,'success_msg':success_msg})



def update_stock(request):
    return render(request,'seller/update_stock.html')


def recent_order(request):
    return render(request,'seller/recent_order.html')


def order_history(request):
    return render(request,'seller/order_history.html')


def profile(request):
    return render(request,'seller/profile.html')


def logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('common:index')







