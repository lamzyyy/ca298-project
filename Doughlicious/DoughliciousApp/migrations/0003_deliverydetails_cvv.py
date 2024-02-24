# Generated by Django 5.0.1 on 2024-02-20 14:20

import DoughliciousApp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoughliciousApp', '0002_cheese_name_sauce_name_size_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverydetails',
            name='cvv',
            field=models.CharField(default='', max_length=3, validators=[DoughliciousApp.validators.validate_cvv]),
        ),
    ]