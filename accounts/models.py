from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='private/users/', blank=True,default='public\defaults/default_avatar.jpg' )
    balance = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    sales_or_purchase = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_restaurant = models.BooleanField(default=False)



    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username



