from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts.models import UserProfile
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


    def clean_restaurant_name(self):
        unique_name = self.cleaned_data['restaurant_name']
        all_restaurants_names = [r.restaurant_name for r in Restaurants.objects.all()]
        if unique_name in all_restaurants_names:
            raise ValidationError("Please use unique restaurant name")
        return unique_name


class AccountEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'balance', ]
