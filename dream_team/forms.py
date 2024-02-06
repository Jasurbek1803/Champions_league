# forms.py

from django import forms
from .models import Player, Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["name"]


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["name", "position"]
