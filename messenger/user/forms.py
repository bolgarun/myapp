from django import forms
from user.models import AuthUser


class AuthUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    password = forms.CharField(max_length=30, required=False)
    
    class Meta:
        model = AuthUser
        fields = ('username', 'password')