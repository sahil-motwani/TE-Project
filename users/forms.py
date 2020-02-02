from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['primary_mobile','date_Of_birth','gender','city', 'state', 'country']
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['image','primary_mobile','city', 'state', 'country']

