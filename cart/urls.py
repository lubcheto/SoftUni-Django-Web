from django.urls import path

from cart.views import cart_view, update_cart, checkout

urlpatterns = (
    path('view/', cart_view, name='cart'),
    path('view/<int:pk>', update_cart, name='update cart'),
    path('checkout/<int:pk>', checkout, name='checkout'),

)
