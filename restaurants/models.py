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


class Restaurants(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250, default="")
    image = models.ImageField(upload_to='public/restaurants/', storage="")

    # category = models.ManyToManyField(CategoryChoices)
    def __str__(self):
        return f'{self.id};{self.name}'

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
