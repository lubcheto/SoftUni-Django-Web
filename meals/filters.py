import django_filters

from meals.models import RestaurantMeals


class FilterMeals(django_filters.FilterSet):
    class Meta:
        model = RestaurantMeals
        fields = '__all__'
        exclude = ['picture','timestamp']