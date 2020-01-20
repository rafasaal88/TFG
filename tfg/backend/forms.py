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
