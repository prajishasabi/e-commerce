from django.shortcuts import render,redirect
from customer.models import Cart
from  seller.models import Product
from common.models import Customer

# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request,'customer/home.html',{'products':products})


def my_cart(request):
    cart = Cart.objects.filter(customer = request.session['customer'])

    return render(request,'customer/my_cart.html',{'cart':cart})



def my_order(request):
    return render(request,'customer/my_order.html')


def change_password(request):
    error_msg = ''
    success_msg = '' 
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if len(new_password) >= 8:
                customer = Customer.objects.get(id = request.session['customer'])
                if customer.password == old_password:
                    Customer.objects.filter(id = request.session['customer']).update(password = new_password)
                    success_msg = 'Password changed successfully'
                else:
                    error_msg = 'Incorrect password'

            else:
                error_msg = 'Password should be 8 characters long'
        else:
            error_msg = 'Password doesn\'t match'

    
            



    return render(request,'customer/change_password.html',{'error_msg':error_msg,'success_msg':success_msg})

    



def products(request,pid):
    error_msg = ''
    product = Product.objects.get(id = pid)

    if request.method =='POST':
        customer  = request.session['customer']
        record_exist = Cart.objects.filter(product = pid, customer = customer ).exists()
        if not record_exist:
            cart = Cart(customer_id = customer , product_id = pid )

            cart.save()
            return redirect('customer:my_cart')
    
        else:
            error_msg = 'Item already in cart'
    
    context = {
        'product':product,
        'message' : error_msg
        }
    return render(request,'customer/product_details.html',context)


def profile(request):
    return render(request,'customer/profile.html')


def logout(request):
    return render(request,'customer/logout.html')



