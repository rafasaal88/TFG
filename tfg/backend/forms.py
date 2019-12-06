from django import forms
from .models import Company


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






