from django.contrib import admin

# Register your models here.
from accounts.models import UserProfile
from cart.models import Cart
from meals.models import RestaurantMeals
from restaurants.models import Restaurants

admin.site.site_header = 'MyProjectDefence admin '


class LikeInlineAdmin(admin.TabularInline):
    model = RestaurantMeals


@admin.register(RestaurantMeals)
class RestaurantMealsAdmin(admin.ModelAdmin):
    list_display = ('meal_name', 'price', 'timestamp')
    list_filter = ('meal_name',)
    search_fields = ("meal_name", "price")


@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ("restaurant_name", "description",)
    list_filter = ("restaurant_name",)
    search_fields = ("restaurant_name", "description")
    inlines = [
        LikeInlineAdmin,
    ]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", 'balance', "sales_or_purchase", 'is_restaurant')
    list_filter = ("user",)
    search_fields = ("user", "sales_or_purchase")


class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)
