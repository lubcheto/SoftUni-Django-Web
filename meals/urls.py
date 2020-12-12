from django.urls import path

from meals.views import MealsListView, MealsCreateView, MealEditView, MealDeleteView, browse_meals_view, \
    surprise_meal_view

urlpatterns = [
    path('list/', MealsListView.as_view(), name='meals list'),
    path('create/', MealsCreateView.as_view(), name='meals create'),
    path('details/<int:pk>', MealEditView.as_view(), name='meals details'),
    path('delete/<int:pk>', MealDeleteView.as_view(), name='meals delete'),
    path('browse/', browse_meals_view, name='browse meals'),
    path('surprise/', surprise_meal_view, name='surprise meal'),

]
