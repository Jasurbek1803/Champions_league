from django.urls import path, include

from .views import games, teams, aboutUs, contactUs

urlpatterns = [
    path("games/", games, name="games"),
    path("teams/", teams, name="teams"),
    path("aboutUs/", aboutUs, name="aboutUs"),
    path("contactUs/", contactUs, name="contactUs"),
]
