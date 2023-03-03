from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Account


class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            "email",
            "username",
            "password1",
            "password2",
        ]


class LogInForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            "email",
            "password",
        ]
