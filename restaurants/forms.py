from django import forms

from restaurants.models import Restaurants


class RestaurantCreateForm(forms.Form):
    class Meta:
        model = Restaurants
        fields = '__all__'


