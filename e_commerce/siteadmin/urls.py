from django.urls import path
from . import views
app_name='siteadmin'
urlpatterns=[
    path('',views.home,name='index'),
    path('approveseller',views.approve_seller,name='approve_seller')

]