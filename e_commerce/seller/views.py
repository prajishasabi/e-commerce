from django.shortcuts import render
from common.models import Seller
from  .models import Product


# Create your views here.

def home(request):
    # seller = Seller.objects.get(id = request.session['seller'])
    seller = Seller.objects.filter(id = request.session['seller']).values('seller_name','pic')
    seller_name = seller[0]['seller_name']
    seller_pic = seller[0]['pic']
    print(seller_pic)
    return render(request,'seller/seller_home.html',{'name':seller_name,'pic': seller_pic})


def catalog(request):
    return render(request,'seller/product_catalog.html')


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








