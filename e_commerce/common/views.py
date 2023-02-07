from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'common/home.html')

def custlogin(request):
    return render(request,'common/customerlogin.html')

def custregistration(request):
    return render(request,'common/customerregist.html')

def sellerlogin(request):
    return render(request,'common/sellerlogin.html')

def sellerregistration(request):
    return render(request,'common/sellerregist.html')

