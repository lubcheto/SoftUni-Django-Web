from django.urls import path

from restaurants.views import RestaurantsListView, RestaurantsCreateView, RestaurantsDetailsView, RestaurantEditView, \
    RestaurantDeleteView

urlpatterns = [
    path('list/', RestaurantsListView.as_view(), name='restaurants list'),
    path('create/', RestaurantsCreateView.as_view(), name='restaurants create'),
    path('details/<int:pk>', RestaurantsDetailsView.as_view(), name='restaurants details'),
    path('edit/<int:pk>', RestaurantEditView.as_view(), name='restaurants edit'),
    path('delete/<int:pk>', RestaurantDeleteView.as_view(), name='restaurants delete'),

]
