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
    buid = forms.CharField(label="8-Digit BUID (only numbers) ", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
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


from django import forms
from .models import Event
class EventForm(forms.ModelForm):
    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        # Remove this validation if latitude is populated by the map
        if latitude is None:
            raise forms.ValidationError('Latitude is required.')
        return round(latitude, 6)  # Round latitude to 6 decimal places

    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        # Remove this validation if longitude is populated by the map
        if longitude is None:
            raise forms.ValidationError('Longitude is required.')
        return round(longitude, 6)  # Round longitude to 6 decimal places

    class Meta:
        model = Event
        fields = ['name', 'img', 'date', 'food_types', 'allergies', 'reservation_limit', 'latitude', 'longitude', 'description', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_description'}),
            
            'img': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'id_img'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'id': 'id_date'}),
            'food_types': forms.Select(attrs={'class': 'form-control', 'id': 'id_food_types'}),
            'allergies': forms.Select(attrs={'class': 'form-control', 'id': 'id_allergies'}),
            'reservation_limit': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_reservation_limit'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter latitude', 'step': 'any', 'id': 'id_latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter longitude', 'step': 'any', 'id': 'id_longitude'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_location', 'placeholder': 'Enter organization name'}) 
        }



    # Remove the custom validation methods as latitude and longitude are optional
    # def clean_latitude(self):
    #     latitude = self.cleaned_data.get('latitude')
    #     if latitude is None:
    #         raise forms.ValidationError('Latitude is required.')
    #     return latitude

    # def clean_longitude(self):
    #     longitude = self.cleaned_data.get('longitude')
    #     if longitude is None:
    #         raise forms.ValidationError('Longitude is required.')
    #     return longitude
