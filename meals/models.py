from django.db import models


# Create your models here.
from accounts.models import UserProfile
from restaurants.models import Restaurants


class RestaurantMeals(models.Model):
    Breakfast = 'breakfast'
    Lunch = 'lunch'
    Dinner = 'dinner'
    Dessert = 'dessert'

    MEAL_TYPES = (
        (Breakfast, 'breakfast'),
        (Lunch, 'lunch'),
        (Dinner, 'dinner'),
        (Dessert, 'dessert')
    )
    meal_name = models.CharField(max_length=30, default='')
    type = models.CharField(max_length=10, choices=MEAL_TYPES, default=Breakfast)
    creator = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField(upload_to='public/meals/', storage="",blank=True)
    is_eatable = True
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} ;{self.meal_name} ;{self.type} ;{self.price}'



