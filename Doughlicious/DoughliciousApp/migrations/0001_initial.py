# Generated by Django 5.0.1 on 2024-02-15 11:39

import DoughliciousApp.models
import DoughliciousApp.validators
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='deliveryDetails',
            fields=[
                ('detailsId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('cardNum', models.CharField(default='', max_length=20, validators=[DoughliciousApp.validators.validate_cardNum])),
                ('expDate', models.DateField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('pizzaId', models.AutoField(primary_key=True, serialize=False)),
                ('crust', models.CharField(choices=[('thin', 'Thin Crust'), ('normal', 'Normal'), ('thick', 'Thick Crust'), ('stuffed', 'Stuffed Crust'), ('gluten free', 'Gluten Free')], max_length=50)),
                ('pepperoni', models.BooleanField(default=False)),
                ('chicken', models.BooleanField(default=False)),
                ('ham', models.BooleanField(default=False)),
                ('pineapple', models.BooleanField(default=False)),
                ('peppers', models.BooleanField(default=False)),
                ('mushroom', models.BooleanField(default=False)),
                ('onions', models.BooleanField(default=False)),
                ('cheese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DoughliciousApp.cheese')),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DoughliciousApp.sauce')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DoughliciousApp.size')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', DoughliciousApp.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateField(auto_now_add=True)),
                ('deliveryDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DoughliciousApp.deliverydetails')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DoughliciousApp.pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]