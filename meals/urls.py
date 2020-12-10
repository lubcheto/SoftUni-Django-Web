from django.urls import path

from meals.views import MealsListView, MealsCreateView, MealEditView, MealDeleteView

urlpatterns = [
    path('list/', MealsListView.as_view(), name='meals list'),
    path('create/', MealsCreateView.as_view(), name='meals create'),
    path('details/<int:pk>', MealEditView.as_view(), name='meals details'),
    path('delete/<int:pk>', MealDeleteView.as_view(), name='meals delete'),


]
