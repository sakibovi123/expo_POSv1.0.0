from django.urls import path
from .cart import Cart
from .cartViews import views

urlpatterns = [
    path('cartview/', views.cart_details, name="cart_details"),
]