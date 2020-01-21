from django import forms
from .models import User, Publicity_campaign


class Publicity_Campaign_Form(forms.ModelForm):
    class Meta:
        model = Publicity_campaign
        fields = [
            'date_start',
            'date_end',
            'description',
            'name',
        ]
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'date_start': forms.DateInput(attrs={'class': 'form-control'}),
        'date_end': forms.DateInput(attrs={'class': 'form-control'}),
       
    }
