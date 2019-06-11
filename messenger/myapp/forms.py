from django import forms
from myapp.models import Messages


class MessagesForm(forms.ModelForm):
    sender = forms.CharField(max_length=30, required=False)
    receiver = forms.CharField(max_length=30, required=False)
    
    
    class Meta:
        model = AuthUser
        fields = ('username', 'password')