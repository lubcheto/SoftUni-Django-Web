from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from accounts.models import UserProfile





class Restaurants(UserProfile):
    restaurant_name = models.CharField(max_length=30)
    description = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.restaurant_name



