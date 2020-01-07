from django import forms
from .models import Company, User


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'nif',
            'name',
            'address',
            'phone_number',
            'mail',
            'web_adress',
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

