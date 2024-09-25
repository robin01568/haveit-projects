# Generated by Django 5.1.1 on 2024-09-23 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='category/category-icon-image')),
                ('total_items', models.IntegerField(blank=True, max_length=10, null=True)),
                ('name', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='Store.productcategory', unique=True)),
            ],
        ),
    ]
