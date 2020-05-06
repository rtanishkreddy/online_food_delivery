from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_number', 'customer_fname', 'customer_lname', 'customer_address_line1', 'customer_address_line2', 'customer_city', 'customer_state', 'customer_zipcode', 'customer_email', 'customer_cellphone',)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('item_name', 'item_description', 'item_price',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_identity', 'order_customer_name', 'order_status', 'order_total_cost',)

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ('detail_order_id', 'detail_item_name', 'detail_quantity', 'detail_spice_level',)