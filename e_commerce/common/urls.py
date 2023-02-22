from django.urls import path
from . import views
app_name='common'
urlpatterns=[
    path('',views.home,name='index'),
    path('custlogin',views.custlogin,name='customer_login'),
    path('custregi',views.custregistration,name='customer_registration'),
    path('sellerlogin',views.sellerlogin,name='seller_login'),
    path('sellerregi',views.sellerregistration,name='seller_registration'),
    path('checkmail',views.check_email,name='check_email')





]