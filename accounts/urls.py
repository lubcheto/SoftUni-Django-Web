from django.urls import path

from accounts.views import RegisterView, LoginViewCustom, AccountDetailsView, AccountEditView, AccountDeleteView
from django.contrib.auth import views

urlpatterns = (
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('details/<int:pk>', AccountDetailsView.as_view(), name='account details'),
    path('edit/<int:pk>', AccountEditView.as_view(), name='account edit'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='account delete'),

)
