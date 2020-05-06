from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


now = timezone.now()
def home(request):
    return render(request, 'users/home.html',
                  {'users': home})

@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'users/customer_list.html',
                  {'customers': customer})


@login_required
def customer_add(request):
   if request.method == "POST":
       form = CustomerForm(request.POST)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.created_date = timezone.now()
           customer.save()
           customers = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'users/customer_list.html',
                         {'customers': customers})
   else:
       form = CustomerForm()
       # print("Else")
   return render(request, 'users/customer_add.html', {'form': form})



@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'users/customer_list.html',
                          {'customers': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'users/customer_edit.html', {'form': form})

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('users:customer_list')


@login_required
def item_list(request):
    item = Item.objects.filter(created_date__lte=timezone.now())
    return render(request, 'users/item_list.html',
                  {'items': item})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        # update
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.updated_date = timezone.now()
            item.save()
            item = Item.objects.filter(created_date__lte=timezone.now())
            return render(request, 'users/item_list.html',
                          {'items': item})
    else:
        # edit
        form = ItemForm(instance=item)
    return render(request, 'users/item_edit.html', {'form': form})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('users:item_list')


@login_required
def order_list(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customers = Customer.objects.filter(created_date__lte=timezone.now())
    orders = Order.objects.filter(order_customer_name=pk)
    return render(request, 'users/order_list.html', {'customers':customers, 'orders': orders})

@login_required
def order_add(request):
   if request.method == "POST":
       form = OrderForm(request.POST)
       if form.is_valid():
           order = form.save(commit=False)
           order.created_date = timezone.now()
           order.save()
           orders = Order.objects.filter(created_date__lte=timezone.now())
           return render(request, 'users/order_list.html',
                         {'orders': orders})
   else:
       form = OrderForm()
       # print("Else")
   return render(request, 'users/order_add.html', {'form': form})




@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        # update
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.updated_date = timezone.now()
            order.save()
            order = Item.objects.filter(created_date__lte=timezone.now())
            return render(request, 'users/order_list.html',
                          {'orders': order})
    else:
        # edit
        form = OrderForm(instance=order)
    return render(request, 'users/order_edit.html', {'form': form})

@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('users:customer_list')


@login_required
def order_detail_list(request, pk):
    order = get_object_or_404(Order, pk=pk)
    orders = Order.objects.filter(created_date__lte=timezone.now())
    orderdetails = OrderDetails.objects.filter(detail_order_id=pk)
    return render(request, 'users/order_detail_list.html', {'orders': orders, 'orderdetails': orderdetails})

@login_required
def order_details_add(request):
   if request.method == "POST":
       form = OrderDetailsForm(request.POST)
       if form.is_valid():
           orderdetail = form.save(commit=False)
           orderdetail.created_date = timezone.now()
           orderdetail.save()
           orderdetails = OrderDetails.objects.filter(created_date__lte=timezone.now())
           return redirect('users:customer_list')
           #return render(request, 'users/customer_list.html',
           #              {'orderdetails': orderdetails})
   else:
       form = OrderDetailsForm()
       # print("Else")
   return render(request, 'users/order_details_add.html', {'form': form})


@login_required
def order_details_delete(request, pk):
    orderdetails = get_object_or_404(OrderDetails, pk=pk)
    orderdetails.delete()
    return redirect('users:customer_list')