from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from restaurants.models import Restaurants


class RestaurantsModelTest(TestCase):
    def test_Restaurant(self):
        restaurant_name = 'aaaaa'
        description = 'bbbb'
        user = User.objects.create()
        restaurant = Restaurants(restaurant_name=restaurant_name,
                              description=description,user=user)

        restaurant.full_clean()
        restaurant.save()

