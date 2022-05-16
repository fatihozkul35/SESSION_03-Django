from django import forms
from .models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','email')
    
class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfile
        exclude = ('user',)
        