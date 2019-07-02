from django.contrib import admin
from .models import Chat, Messages

admin.site.register(Messages)
admin.site.register(Chat)