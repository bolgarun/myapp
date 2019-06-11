from django.urls import path
from myapp.views import index, all_users


urlpatterns = [
    path('', index, name='index'),
    path('all-users', all_users, name='all-users'),
]