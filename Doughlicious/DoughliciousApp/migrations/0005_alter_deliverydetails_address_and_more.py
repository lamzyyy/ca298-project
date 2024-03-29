# Generated by Django 5.0.1 on 2024-02-24 11:15

import DoughliciousApp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoughliciousApp', '0004_alter_deliverydetails_expdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverydetails',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='deliverydetails',
            name='name',
            field=models.CharField(default='', max_length=50, validators=[DoughliciousApp.validators.validate_names]),
        ),
    ]
