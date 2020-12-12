from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from meals.models import RestaurantMeals


class Cart(models.Model):
    products = models.ManyToManyField(RestaurantMeals, null = True,blank=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.id



