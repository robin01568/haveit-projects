# Generated by Django 5.1.1 on 2024-10-05 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentApp', '0001_initial'),
        ('Store', '0031_order_payment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.order'),
        ),
    ]
