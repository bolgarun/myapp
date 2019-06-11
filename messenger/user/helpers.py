from django.http import HttpResponse, HttpResponseRedirect


def valid_password(password):
    if len(password) < 5:
        return HttpResponse('Faild password: your password to small')
    for x in password:
        if not x.isalpha() and not x.isdigit() and not x.islower() and not x.islower():
          return HttpResponse('Faild password: your password have not letters')
    return password
