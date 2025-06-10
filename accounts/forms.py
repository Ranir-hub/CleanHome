from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm
from django.contrib.auth import password_validation

from accounts.models import CustomUser

class LoginForm(AuthenticationForm):
    username = UsernameField(label="Логин", widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control mb-3"}))
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control mb-3"}),
    )

class SignUpForm(UserCreationForm):
    username = UsernameField(label="Логин", widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control mb-3"}))
    email = forms.EmailField(
        label="Почта",
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control mb-3"}),
    )
    phone = forms.CharField(
        label="Номер телефона",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
    )
    password1 = forms.CharField(
        label="Пароль",
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control mb-3"}),
        help_text="Ваш пароль не должен быть слишком похож на вашу другую личную информацию.<br>\
                    Ваш пароль должен содержать не менее 8 символов.<br>\
                    Ваш пароль не может быть общеупотребимым паролем.<br>\
                    Ваш пароль не может состоять только из цифр.",
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control mb-3"}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')
