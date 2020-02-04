from django import forms
from .models import User, Publicity_campaign, UserProfile, Product


class Publicity_Campaign_Form(forms.ModelForm):
    class Meta:
        model = Publicity_campaign
        fields = [
            'date_start',
            'date_end',
            'description',
            'name',
            'image',
            'user'
        ]
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'date_start': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        'date_end': forms.DateInput(attrs={'class': 'form-control'}),
        'user': forms.TextInput(attrs={'class': 'form-control'}),
       
    }

class User_Form_Email(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
        ]
        widgets = {
        'email': forms.TextInput(attrs={'class': 'form-control'}),       
    }        

class User_Form_Name(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]
        widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),   
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),     
    }

class User_Profile_Form(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = [
            'image',
        ]


class User_Profile_Create(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_staff'
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
            user = super(User_Profile_Create, self).save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user


class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'price',
            'description',
            'date',
            'picture',
        ]
        widgets = {
            'price': forms.FloatField(),
            'description': forms.TextInput(),
            'date': forms.DateField(),
        }





