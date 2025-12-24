from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class RegisterForm(UserCreationForm):
    avatar = forms.ImageField(required=False)
    about = forms.CharField(
        widget=forms.Textarea,
        required=False
    )
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'about', 'avatar', 'password1', 'password2', "email")

class InitiativeForm(forms.ModelForm):
    class Meta:
        model = initiative
        fields = ['title', 'image', 'adres', 'text']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название инициативы'
            }),
            'adres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Описание'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['text']
