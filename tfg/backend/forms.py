from django import forms
from .models import User, Publicity_campaign

"""
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
"""




class Publicity_Campaign_Form(forms.ModelForm):
    class Meta:
        model = Publicity_campaign
        fields = [
            'date_start',
            'date_end',
            'description',
            'name',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

