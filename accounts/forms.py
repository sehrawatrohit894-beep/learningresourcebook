from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=60, required=True, label="Full name")
    phone = forms.CharField(max_length=15, required=True, label="Phone number")

    class Meta:
        model = User
        fields = ["first_name", "username", "email", "phone", "password1", "password2"]
