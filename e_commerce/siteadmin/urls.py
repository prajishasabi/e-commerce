from django.urls import path
from . import views
app_name='siteadmin'
urlpatterns=[
    path('',views.home,name='index'),
    path('approveseller',views.approve_seller,name='approve_seller'),
    path('viewseller',views.view_seller,name='view_seller'),
    path('viewcustomer',views.view_customer,name='view_customer'),
    path('index',views.index,name='index')




]