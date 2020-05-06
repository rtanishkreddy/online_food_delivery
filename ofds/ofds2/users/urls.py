from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'users'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_add, name='customer_add'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('item_list', views.item_list, name='item_list'),
    path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('customer/<int:pk>/order_list/', views.order_list, name='order_list'),
    path('order/create/', views.order_add, name='order_add'),
    path('order/<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('customer/order/<int:pk>/details/', views.order_detail_list, name='order_detail_list'),
    path('orderdetails/create/', views.order_details_add, name='order_details_add'),
    path('orderdetails/<int:pk>/delete/', views.order_details_delete, name='order_details_delete'),
]
