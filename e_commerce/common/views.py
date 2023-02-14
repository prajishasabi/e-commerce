from django.shortcuts import render,redirect
from .models import Customer
from .models import Seller

# Create your views here.

def home(request):
    return render(request,'common/home.html')

def custlogin(request):
    msg = ""


    if request.method =='POST':

        email = request.POST['email']
        password = request.POST['password']
        # request.session['customer'] = customer.id



        try:
            customer = Customer.objects.get(email = email,password = password)
            return redirect('customer:index')
        except Exception as e:
            msg = 'email or password incorrect'

    return render(request,'common/customerlogin.html',{'message':msg})


def custregistration(request):
    msg = ''
    if request.method == 'POST':
        cname = request.POST['custmer_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']
        email_exist = Customer.objects.filter(email = email).exists()

        if not email_exist:


            customer = Customer(customer_name = cname,email = email, address = address, phone = phone, gender = gender, password = password)
            customer.save()
        else:
            msg = 'Email already Used! try with another valid email'
            

    return render(request,'common/customerregist.html',{'message':msg})

def sellerlogin(request):
    msg = ''
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            seller = Seller.objects.get(user_name = username,password = password)
            request.session['seller'] = seller.id
            return redirect('seller:index')
        except Exception as e:
            msg = 'username or password incorrect'

    return render(request,'common/sellerlogin.html',{'message':msg})

def sellerregistration(request):
    msg = ''
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
        # image = request.FILES['image']

        if 'image' in request.FILES:
            image = request.FILES['image']
            seller = Seller(seller_name = sname,email = email, address = address, 
                        phone = phone, gender = gender, company_name = company_name, 
                        holder_name = holder_name, ifsc = ifsc , branch = branch, account_number = acc_number,
                        pic = image)
        else:
             seller = Seller(seller_name = sname,email = email, address = address, 
                        phone = phone, gender = gender, company_name = company_name, 
                        holder_name = holder_name, ifsc = ifsc , branch = branch, account_number = acc_number,
                        )
        seller.save()
        msg = 'You have registered successfully'



    return render(request,'common/sellerregist.html',{'message':msg})

