# Generated by Django 5.1.1 on 2024-09-23 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_remove_categorys_total_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorys',
            name='total_items',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
