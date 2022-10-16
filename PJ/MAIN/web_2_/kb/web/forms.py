from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username","age","child","Marriage","work","work_address","hope_address","password1", "password2", "email")

