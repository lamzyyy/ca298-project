# Generated by Django 5.0.1 on 2024-02-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoughliciousApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sauce',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='size',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]