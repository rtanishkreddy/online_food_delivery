from django.contrib import admin

from .models import Customer
from .models import Item
from .models import Order
from .models import OrderDetails

class CustomerList(admin.ModelAdmin):
    list_display = ('customer_number', 'customer_fname', 'customer_city', 'customer_cellphone')
    list_filter = ('customer_number', 'customer_fname', 'customer_lname', 'customer_city')
    search_fields = ('customer_number', 'customer_fname', 'customer_lname')
    ordering = ['customer_number']


class ItemList(admin.ModelAdmin):
    list_display = ('item_name', 'item_description', 'item_price')
    list_filter = ('item_name', 'item_description', 'item_price')
    search_fields = ('item_name', 'item_description', 'item_price')
    ordering = ['item_name']

class OrderList(admin.ModelAdmin):
    list_display = ('order_customer_name', 'order_status', 'order_total_cost')
    list_filter = ('order_customer_name', 'order_status', 'order_total_cost')
    search_fields = ('order_customer_name', 'order_status', 'order_total_cost')
    ordering = ['order_customer_name']

class OrderDetailsList(admin.ModelAdmin):
    list_display = ('detail_order_id', 'detail_item_name', 'detail_quantity', 'detail_spice_level')
    list_filter = ('detail_order_id', 'detail_item_name', 'detail_quantity', 'detail_spice_level')
    search_fields = ('detail_order_id', 'detail_item_name', 'detail_quantity', 'detail_spice_level')
    ordering = ['detail_order_id']


admin.site.register(Customer, CustomerList)
admin.site.register(Item, ItemList)
admin.site.register(Order, OrderList)
admin.site.register(OrderDetails, OrderDetailsList)

