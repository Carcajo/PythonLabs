from django import forms
from django.core.validators import RegexValidator

from .models import Order


class OrderCreateForm(forms.ModelForm):

    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="Адрес", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_regex = RegexValidator(regex="\+375[0-9]{9}", message="Введите номер телефона в формате +375000000000")
    phone_number = forms.CharField(label='Номер телефона', validators=[phone_regex],
                                   max_length=13, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address']
