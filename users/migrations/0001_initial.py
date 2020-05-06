# Generated by Django 2.0.5 on 2020-05-06 06:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_number', models.IntegerField()),
                ('customer_fname', models.CharField(max_length=50)),
                ('customer_lname', models.CharField(max_length=50)),
                ('customer_address_line1', models.CharField(max_length=200)),
                ('customer_address_line2', models.CharField(blank=True, max_length=200)),
                ('customer_city', models.CharField(max_length=50)),
                ('customer_state', models.CharField(max_length=50)),
                ('customer_zipcode', models.CharField(max_length=10)),
                ('customer_email', models.EmailField(max_length=200)),
                ('customer_cellphone', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_description', models.CharField(max_length=500)),
                ('item_price', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_identity', models.CharField(max_length=100)),
                ('order_status', models.CharField(max_length=100)),
                ('order_total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('order_customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='users.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_quantity', models.IntegerField()),
                ('detail_spice_level', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('detail_item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemname', to='users.Item')),
                ('detail_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderid', to='users.Order')),
            ],
        ),
    ]
