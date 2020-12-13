from django.test import TestCase

# Create your tests here.
from cart.models import Cart
from meals.models import RestaurantMeals


class CartModelTest(TestCase):
    def test_Cart(self):
        total = 20.00
        active = True
        cart = Cart(total = total,active=active)
        cart.full_clean()
        cart.save()



