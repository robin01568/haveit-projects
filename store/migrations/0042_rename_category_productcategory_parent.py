# Generated by Django 5.1.1 on 2024-10-09 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0041_productcategory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='category',
            new_name='parent',
        ),
    ]
