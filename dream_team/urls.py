from django.urls import path, include
from .views import dream_team, add_players, full_formation

urlpatterns = [
    path("", dream_team, name="dream_team"),
    path("add_players/", add_players, name="add_players"),
    path("add_players/<int:team_id>/", add_players, name="add_players"),
    path("full_formation/", full_formation, name="full_formation"),
    path("full_formation/<int:team_id>/", full_formation, name="full_formation"),
]
