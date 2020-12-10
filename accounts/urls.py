from django.urls import path

from accounts.views import RegisterView, LoginViewCustom
from django.contrib.auth import views

urlpatterns = (
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register user'),  # this is class based view

)
