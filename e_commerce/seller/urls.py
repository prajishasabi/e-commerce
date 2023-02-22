from django.urls import path
from . import views
app_name='seller'
urlpatterns=[
    path('home',views.home,name='index'),
    path('catalog',views.catalog,name='catalog'),
    path('addproduct',views.add_product,name='add_product'),
    path('changepassword',views.change_password,name='change_password'),
    path('updatestock',views.update_stock,name='update_stock'),
    path('recentorder',views.recent_order,name='recent_order'),
    path('orderhistory',views.order_history,name='order_history'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout')





]