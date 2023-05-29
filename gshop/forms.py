from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_regex = RegexValidator(regex="\+375[0-9]{9}", message="Введите номер телефона в формате +375000000000")
    phone_number = forms.CharField(label='Номер телефона', validators=[phone_regex],
                                    max_length=13, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Почта", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class':
                                                                                                   'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


