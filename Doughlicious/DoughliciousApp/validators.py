def validate_cardNum(cardnumber): 
    cardnumber = cardnumber.replace(' ', '')
    if len(cardnumber) != 16:
        raise ValueError('Card number must be 16 digits long.')
    
    elif not cardnumber.isdigit():
        raise ValueError('card numbers must contain only numbers ')