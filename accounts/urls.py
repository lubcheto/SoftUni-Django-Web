from django.urls import path

from accounts.views import RegisterView
from django.contrib.auth import views

urlpatterns = (
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register user'),  # this is class based view

)
