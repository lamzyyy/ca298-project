from datetime import datetime
from django.core.exceptions import ValidationError


def validate_cardNum(cardnumber): 
    cardnumber = cardnumber.replace(' ', '')
    if len(cardnumber) != 16:
        raise ValueError('Card number must be 16 digits long.')
    
    elif not cardnumber.isdigit():
        raise ValueError('card numbers must contain only numbers ')

def validate_cvv(cvv):
    if cvv.isdigit() == False or len(cvv) < 3: 
        raise ValueError('cvv numbers must contain only numbers and must be 3 characters')


def validate_date_format(value):
    if len(str(value.year)) > 4:
        raise ValidationError('Year must be 4 digits or fewer.')

def validate_names(name):
    name = name.replace(' ', '')
    if not name.isalpha():
        raise ValueError('name field must not contain numerals or special characters')
    