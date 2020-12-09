from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from accounts.models import UserProfile


#
# class CategoryChoices(models.Model):
#     choice1 = models.CharField(max_length=30, default='')
#     choice2 = models.CharField(max_length=30, default='')
#     choice3 = models.CharField(max_length=30, default='')
#     choice4 = models.CharField(max_length=30, default='')
#     choice5 = models.CharField(max_length=30, default='')


class Restaurants(UserProfile):
    restaurant_name = models.CharField(max_length=30)
    description = models.CharField(max_length=250, default="")
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile_picture = models.ImageField(upload_to='public/restaurants/', storage="")
    # balance = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    # amount_of_sale = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return f'{self.id}'




# class LikeRestaurant(models.Model):
#     pet = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
#     test = models.CharField(max_length=2)
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#
#
# class CommentRestaurant(models.Model):
#     pet = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
#     text = models.TextField(blank=False)
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
