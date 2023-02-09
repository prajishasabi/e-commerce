from django.shortcuts import render
from .models import Customer
from .models import Seller

# Create your views here.

def home(request):
    return render(request,'common/home.html')

def custlogin(request):
    return render(request,'common/customerlogin.html')

def custregistration(request):
    if request.method == 'POST':
        cname = request.POST['custmer_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']


        customer = Customer(customer_name = cname,email = email, address = address, phone = phone, gender = gender, password = password)
        customer.save()


    return render(request,'common/customerregist.html')

def sellerlogin(request):
    return render(request,'common/sellerlogin.html')

def sellerregistration(request):
    if request.method == 'POST':
        sname = request.POST['seller_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        gender = request.POST['gender']
        company_name = request.POST['company_name']
        holder_name = request.POST['holder_name']
        ifsc = request.POST['ifsc']
        branch = request.POST['branch']
        acc_number = request.POST['acc_number']
        image = request.FILES['image']

        seller = Seller(seller_name = sname,email = email, address = address, phone = phone, gender = gender, company_name = company_name, holder_name = holder_name, ifsc = ifsc , branch = branch, account_number = acc_number, pic = image)
        seller.save()



    return render(request,'common/sellerregist.html')

