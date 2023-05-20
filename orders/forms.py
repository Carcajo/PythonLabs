from django import forms
from django.core.validators import RegexValidator

from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Surname", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        label="Address", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone_regex = RegexValidator(
        regex="\+375[0-9]{9}",
        message="Enter your phone number in the format +375000000000",
    )
    phone_number = forms.CharField(
        label="Phone number",
        validators=[phone_regex],
        max_length=13,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Order
        fields = ["first_name", "last_name", "address"]
