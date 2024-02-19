# forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import *
from django.db import transaction

class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.email = self.cleaned_data['username']
        user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

class createPizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'pepperoni', 'chicken', 'ham', 'pineapple', 'peppers', 'mushroom', 'onions']

        widgets = {
            'size': forms.Select(attrs={'class': 'form-select'}),
            'crust': forms.Select(attrs={'class': 'form-select'}),
            'sauce': forms.Select(attrs={'class': 'form-select'}),
            'cheese': forms.Select(attrs={'class': 'form-select'}),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pepperoni'].label = 'Pepperoni'
        self.fields['chicken'].label = 'Chicken'
        self.fields['ham'].label = 'Ham'
        self.fields['pineapple'].label = 'Pineapple'
        self.fields['peppers'].label = 'Peppers'
        self.fields['mushroom'].label = 'Mushrooms'
        self.fields['onions'].label = 'Onions'


class createDeliveryDetailsForm(forms.ModelForm):
    expDate = forms.DateField(label='Select a Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    class Meta:
        model = deliveryDetails
        fields = ['name', 'address', 'cardNum', 'expDate']

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'})
    )
    cardNum = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Number'})
    )
    expDate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Expiration Date'})
    )