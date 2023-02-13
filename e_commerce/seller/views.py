from django.shortcuts import render
from common.models import Seller


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
    if request.method == 'POST':
        product_name = request.POST['product_name']
        description = request.POST['description']
        stock = request.POST['stock']
        price = request.POST['price']
        image = request.FILES['image']

        

       

    return render(request,'common/customerregist.html')
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








