from django.shortcuts import render
from common.models import Seller
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


def home(request):
    sellers = Seller.objects.all().count()


    return render(request,'siteadmin/home.html',{'seller_count':sellers})

@api_view(['GET'])
def index(request):
    message = "You have created an API"
    return Response(message)


def approve_seller(request):
    sellers = Seller.objects.filter(status = 'pending') 

    if request.method == 'POST':
        seller_id = request.POST['seller_id']
        seller = Seller.objects.get(id = seller_id)

        if 'approve' in request.POST:
            # logic when approve button clicked
            user_name = randint(1111,9999)
            password = 'sel-' + str(user_name) + str(seller.phone)[5:]

           
            seller.status = 'approved' # sql update query
            seller.user_name = user_name
            seller.password = password
            seller.save()
            
            mail_subject = "Account Approval"
            message_body = "Hi your account has been approved by Admin,you can now login with username " + str(user_name) + " and temporary password " + password 

           
        if 'reject' in request.POST:
            
            seller.status = 'rejected'
            seller.save()
            mail_subject = 'Account Rejected'
            message_body = 'sorry!we can not approve your request right now'
             

        send_mail(
            subject = mail_subject,
            message = message_body,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [seller.email]
            )

            

    return render(request,'siteadmin/approve_seller.html',{'sellers_list':sellers})


def view_seller(request):
    sellers = Seller.objects.filter(status = 'approved') 
    return render(request,'siteadmin/view_seller.html',{'sellers_list':sellers})


def view_customer(request):
    return render(request,'siteadmin/view_customer.html')