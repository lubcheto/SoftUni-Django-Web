from django.contrib import admin

# Register your models here.
from accounts.models import UserProfile
from meals.models import RestaurantMeals
from restaurants.models import Restaurants


class LikeInlineAdmin(admin.TabularInline):
    model = RestaurantMeals

class RestaurantsAdmin(admin.ModelAdmin):
    fields = ('type', 'name')
    list_display = ('id','name')
    list_filter = ('name',)
    inlines = [
        LikeInlineAdmin,
    ]


admin.site.register(Restaurants)
admin.site.register(RestaurantMeals)
admin.site.register(UserProfile)
admin.site.site_header = 'MyProjectDefence admin '