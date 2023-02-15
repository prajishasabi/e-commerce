from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('home',views.home,name='index'),
    path('mycart',views.my_cart,name='my_cart'),
    path('myorder',views.my_order,name='my_order'),
    path('changepassword',views.change_password,name='change_password'),
    path('product/<int:pid>',views.products,name='products'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout')



]