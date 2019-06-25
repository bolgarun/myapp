from django.http import HttpResponse


def valid_password(password):
    letter = False
    number = False
    up = False
    low = False
    for x in password:
        if x.isalpha():
            letter = True
        if x.isdigit():
            number = True
        if x.isupper():
            up = True
        if x.islower():
            low = True

    if letter is True and number is True and up is True and low is True and len(password) > 5:
        return password
    return HttpResponse('Faild password: try again with password')