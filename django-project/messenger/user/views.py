from django.contrib.auth import authenticate, login, logout
from user.models import AuthUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
    return render(
        request, 'user/register.html',
        {'user_form': user_form}
        )


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
    return render(
        request, 'user/user_profile.html',
        {'user_profile': user_profile}
        )


def message_create(request):
    id_recipient = request.POST['recipient']
    recipient = AuthUser.objects.filter(id=id_recipient).get()
    sender_chat = Chat.objects.filter(users=request.user)
    recipient_chat = Chat.objects.filter(users=recipient)
    intersect = list(set(sender_chat).intersection(recipient_chat))
    if intersect:
        message = Messages(
            chat=intersect[0],
            author=request.user,
            text=request.POST['text'],
            )
        chat_id = intersect[0].id
        message.save()
    else:
        chat = Chat()
        chat.save()
        chat.users.add(request.user)
        chat.users.add(recipient)
        chat.save()
        message = Messages(
            chat=chat,
            author=request.user,
            text=request.POST['text'],
            )
        chat_id = chat.id
        message.save()
    return HttpResponseRedirect(reverse(
        'chat-profile-view',
        kwargs={'chat_id': chat_id}))


def chat_profile_view(request, chat_id):
    user_chat = Chat.objects.filter(id=chat_id)
    for i in user_chat:
        i.assign_recipient(request.user)
    return render(
        request, 'user/chat.html',
        {'user_chat': user_chat})


def all_chat(request):
    users = AuthUser.objects.all().exclude(username=request.user.username)
    chats = request.user.chat_set.all()
    for c in chats:
        c.assign_recipient(request.user)
    return render(request, 'user/all_chat.html', {'chats': chats, 'users': users})


def add_new_chat(request):
    user_id = request.POST.getlist("user")
    if len(user_id) < 2:
        sender_chat = Chat.objects.filter(users=request.user)
        recipient_chat = Chat.objects.filter(users=''.join(user_id))
        intersect = list(set(sender_chat).intersection(recipient_chat))
        if not intersect:
            chat = Chat()
            chat.save()
            chat.users.add(request.user)
            chat.users.add(''.join(user_id))

    return HttpResponseRedirect(reverse('all-chat'))

def add_new_group_chat(request):
    user_id = request.POST.getlist("user-group")
    if len(user_id) > 1:
        chat = Chat()
        chat.save()
        chat.users.add(request.user)
        chat.name_chat = request.POST['text']
        for u in user_id:
            chat.users.add(u)
            chat.save()

    return HttpResponseRedirect(reverse('all-chat'))


def create_message_in_chat(request):
    chat_id = request.POST['user_chat']
    user_chat = Chat.objects.filter(id=chat_id)
    message = Messages(
            chat=user_chat[0],
            author=request.user,
            text=request.POST['text'],
            )
    message.save()
    return HttpResponseRedirect(reverse(
        'chat-profile-view',
        kwargs={'chat_id': chat_id}))
