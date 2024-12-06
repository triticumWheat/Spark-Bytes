from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from spark_bytes_app.models import Event


# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    buid = forms.CharField(label="BUID", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    img = forms.ImageField(label="Profile Picture", required=True)

    class Meta:
        model = User  # Make sure User model is the custom user model if you have one
        fields = ['username', 'email', 'password1', 'password2', 'buid', 'img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply bootstrap classes to all fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'img', 'location', 'date', 'food_types', 'allergies', 'reservation_limit']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'food_types': forms.Select(attrs={'class': 'form-control'}),
            'allergies': forms.Select(attrs={'class': 'form-control'}),
            'reservation_limit': forms.NumberInput(attrs={'class': 'form-control'}),
        }

