from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import UserProfile

# Create your tests here.

'''Models'''
class UserProfileModelTest(TestCase):
    def test_create_profile_with_fields(self):
        profile_picture = "1.img"
        balance = 20.00
        sales_or_purchase =2
        is_restaurant=True
        user = User.objects.create()
        profile = UserProfile(profile_picture=profile_picture,
                              balance=balance,
                              sales_or_purchase=sales_or_purchase,
                              is_restaurant=is_restaurant,
                              user=user)

        profile.full_clean()
        profile.save()







