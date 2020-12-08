

from django.urls import path

from restaurants.views import RestaurantsListView, RestaurantsCreateView

urlpatterns = [
    path('list/',RestaurantsListView.as_view(), name = 'restaurants list'),
    path('create/',RestaurantsCreateView.as_view(), name = 'restaurants create'),

]
