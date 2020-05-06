from django.db import models

from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    customer_number = models.IntegerField(blank=False, null=False)
    customer_fname = models.CharField(blank=False, max_length=50)
    customer_lname = models.CharField(max_length=50)
    customer_address_line1 = models.CharField(blank=False, max_length=200)
    customer_address_line2 = models.CharField(blank=True, max_length=200)
    customer_city = models.CharField(blank=False, max_length=50)
    customer_state = models.CharField(blank=False, max_length=50)
    customer_zipcode = models.CharField(blank=False, max_length=10)
    customer_email = models.EmailField(max_length=200)
    customer_cellphone = models.CharField(blank=False, max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer_number)


class Item(models.Model):
    item_name = models.CharField(blank=False, max_length=50)
    item_description = models.CharField(max_length=500)
    item_price = models.CharField(blank=False, max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.item_name)


class Order(models.Model):
    order_identity = models.CharField(max_length=100, blank=False)
    order_customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_status = models.CharField(max_length=100, blank=False)
    order_total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.order_identity)


class OrderDetails(models.Model):
    detail_order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderid')
    detail_item_name = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='itemname')
    detail_quantity = models.IntegerField(blank=False)
    detail_spice_level = models.IntegerField()
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.detail_order_id)
