from django.contrib.auth import authenticate, login, logout
from user.models import AuthUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from myapp.views import index, all_users
from user.forms import AuthUserForm
from user.helpers import valid_password
from myapp.models import Messages, Chat



@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        user_form = AuthUserForm(data=request.POST)
        user_password = user_form.data.get('password')
        if valid_password(user_password) == user_password and user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect('index')
        else:
            print(user_form.errors)

    else:
        user_form = AuthUserForm()
    return render(request,'user/register.html',
                          {'user_form':user_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('all-users'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user/login.html', {})

def user_detail(request, user_id):
    user_profile = AuthUser.objects.filter(id=user_id).get()
    return render(request, 'user/user_profile.html', {'user_profile': user_profile})


def message_create(request):
    receiver_id = request.POST['recipient']
    data_receiver = AuthUser.objects.filter(id=receiver_id).get()
    sms = Messages(
        sender = request.user,
        receiver = data_receiver,
        message = request.POST['message'],
        )
    print(sms)
    sms.save()

    return HttpResponseRedirect(reverse('mychat'))

def mychat(request):
    all_messages = Messages.objects.all()
    return render(request, 'user/chat.html')
