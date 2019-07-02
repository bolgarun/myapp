from django.urls import path
from user.views import user_login, register, user_logout,\
    special, user_detail, message_create, chat_profile_view,\
    all_chat, add_new_chat, add_new_group_chat, create_message_in_chat


urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout', user_logout, name='logout'),
    path('special', special, name='special'),
    path('profile/<int:user_id>/', user_detail, name='user-page'),
    path('message-create', message_create, name='message-create'),
    path(
        'chat-profile-view/<int:chat_id>/',
        chat_profile_view,
        name='chat-profile-view'
        ),
    path('all-chat', all_chat, name='all-chat'),
    path('add-new-chat', add_new_chat, name='add-new-chat'),
    path('add-new-group-chat', add_new_group_chat, name='add-new-group-chat'),
    path('create-message-in-chat', create_message_in_chat, name='create-message-in-chat')
]
