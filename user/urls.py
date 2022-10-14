from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/',views.signin),
    path('home/',views.home),
]
