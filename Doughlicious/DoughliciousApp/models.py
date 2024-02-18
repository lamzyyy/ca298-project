from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.core import validators
from .validators import *
# models.py


#... any other imports

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class Size(models.Model):
    name = models.CharField(default=(""), max_length=100)
    
    def __str__(self):
        return self.name 
    

class Sauce(models.Model):
    name = models.CharField(default=(""), max_length=100)
    def __str__(self):
        return self.name 

class Cheese(models.Model):
    name = models.CharField(default=(""), max_length=100) 
    
    def __str__(self):
        return self.name 
    
class Pizza(models.Model):
   pizzaId =  models.AutoField(primary_key=True)
   
   CRUST_CHOICES = [
        ('thin', 'Thin Crust'),
        ('normal', 'Normal'),
        ('thick', 'Thick Crust'),
        ('stuffed', 'Stuffed Crust'),       
        ('gluten free', 'Gluten Free'),]

   size =  models.ForeignKey("DoughliciousApp.Size", on_delete=models.CASCADE)
   sauce =  models.ForeignKey("DoughliciousApp.Sauce", on_delete=models.CASCADE)
   cheese =  models.ForeignKey("DoughliciousApp.Cheese", on_delete=models.CASCADE)
   crust = models.CharField(choices=CRUST_CHOICES, max_length=50)
   pepperoni = models.BooleanField(default=False)
   chicken = models.BooleanField(default=False)
   ham = models.BooleanField(default=False)
   pineapple = models.BooleanField(default=False)
   peppers = models.BooleanField(default=False)
   mushroom = models.BooleanField(default=False) 
   onions = models.BooleanField(default=False)

   def __str__(self) -> str:
        
        toppings = [
        ('Pepperoni ' if self.pepperoni else ''),
        ('Chicken ' if self.chicken else ''),
        ('Ham ' if self.ham else ''),
        ('Pineapple ' if self.pineapple else ''),
        ('Peppers ' if self.peppers else ''),
        ('Mushrooms ' if self.mushroom else ''),
        ('Onions ' if self.onions else '')]

        chosen_toppings = [t for t in toppings if t]
        chosen_toppings = ', '.join(chosen_toppings)
        return ('Size: {},  Crust Type: {},  Sauce: {},  Chosen Toppings: {}. ').format(self.size, self.crust, self.sauce, chosen_toppings)

    
class deliveryDetails(models.Model):
    detailsId = models.AutoField(primary_key=True)
    name = models.CharField(default=(""), max_length=50)
    address = models.CharField(default=(""), max_length=50)
    cardNum = models.CharField( default = '', max_length=20, validators=[validate_cardNum])
    expDate = models.DateField(default=(""), auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return ('Name: {}. living at {}').format(self.name, self.address)

class order(models.Model):
    user = models.ForeignKey("DoughliciousApp.User", on_delete=models.CASCADE)
    deliveryDetails =  models.ForeignKey("DoughliciousApp.deliveryDetails", on_delete=models.CASCADE)
    pizza = models.ForeignKey("DoughliciousApp.Pizza", on_delete=models.CASCADE)
    orderDate = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return ("{} ordered: {} to {} on {}").format(self.deliveryDetails.name, str(self.pizza), self.deliveryDetails.address, self.orderDate)