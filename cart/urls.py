from django.contrib import admin
from django.urls import path
from .views import CartView, CartRemove


urlpatterns = [
    path('add/', CartView.as_view(), name="cart-add"),
    path('remove/', CartRemove.as_view(), name="cart-remove")
]
