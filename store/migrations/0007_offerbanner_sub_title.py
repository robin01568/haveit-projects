# Generated by Django 5.1.1 on 2024-09-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_banner_offerbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerbanner',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
