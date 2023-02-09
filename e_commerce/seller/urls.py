from django.urls import path
from . import views
app_name='seller'
urlpatterns=[
    path('home',views.home,name='index'),
    path('catalog',views.catalog,name='catalog'),
    path('addproduct',views.add_product,name='add_product'),
    path('changepassword',views.change_password,name='change_password'),



]