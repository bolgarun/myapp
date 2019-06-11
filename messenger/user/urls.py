from django.urls import path
from user.views import user_login, register, user_logout, special, user_detail, message_create, mychat


urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout', user_logout, name='logout'),
    path('special', special, name='special'),
    path('profile/<int:user_id>/', user_detail, name='user-page'),
    path('message-create', message_create, name='message-create'),
    path('mychat', mychat, name='mychat'),
]
