


from django.urls import path

from meals.views import MealsListView, MealsCreateView

urlpatterns = [
    path('list/',MealsListView.as_view(), name = 'meals list'),
    path('create/', MealsCreateView.as_view(), name ='meals create'),

]
