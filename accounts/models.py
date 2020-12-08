from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='private/users/', blank=True, )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    amount_of_purchases = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    def __str__(self):
        return self.user.username



