from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from restaurants.models import Restaurants


class RegisterForm(UserCreationForm):
    CHOICES = [('1', 'Restaurant'), ('2', 'Buyer')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class RestaurantEditForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['restaurant_name', 'description', 'profile_picture']
