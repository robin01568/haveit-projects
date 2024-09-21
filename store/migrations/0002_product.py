# Generated by Django 5.1.1 on 2024-09-21 08:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('product_code', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='prodect/prodect-image')),
                ('hover_image', models.ImageField(upload_to='prodect/prodect-image')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='prodect/prodect-extra-image')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='prodect/prodect-extra-image')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='prodect/prodect-extra-image')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='prodect/prodect-extra-image')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='prodect/prodect-extra-image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('short_description', models.TextField()),
                ('detail_description', models.TextField()),
                ('specific_description', models.TextField(blank=True, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productcategory')),
                ('color', models.ManyToManyField(to='store.color')),
                ('size', models.ManyToManyField(to='store.size')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
