from django.forms import ModelForm
from django import forms
from .models import GroupMessage

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'class': 'p-4 text-back', 'placeholder': 'Skriv meddelande...', 'max_length': '300', 'autofocus': 'true'}),
        }