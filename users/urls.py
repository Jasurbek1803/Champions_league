from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import index, registration, login

urlpatterns = [
    path("", index, name="index"),
    path("registration/", registration, name="registration"),
    path("login/", login, name="login"),
]
