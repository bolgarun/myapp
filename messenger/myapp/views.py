from django.shortcuts import render
from user.models import AuthUser


def index(request):
    return render(request, 'myapp/index.html')


def all_users(request):
    all_users = AuthUser.objects.all().exclude(username=request.user.username)
    return render(
        request, 'myapp/messenger.html', context={'users': all_users}
        )