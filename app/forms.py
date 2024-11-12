from django import forms
from .models import Book

class FormBook (forms.ModelForm):
    class Meta:
        model=Book
        fields=['titre',
                'description',
                'image']
        widgets={
            'titre':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class registerform(UserCreationForm):
    first_name=forms.CharField(max_length=15)
    last_name=forms.CharField(max_length=15)
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')

from django import forms
from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))

