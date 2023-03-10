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
    path('logout',views.logout,name='logout'),
    path('cart/remove/<int:c_id>',views.remove_cart,name='remove_cart'),
    path('order_details',views.order_details,name='order_deatils'),
    path('payment',views.payment,name='payment')



]