# dream_team/models.py
from django.db import models
from users.models import MyUser  # Import your User model


class Team(models.Model):
    name = models.CharField(max_length=100)
    users = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name="teams", default=1
    )

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(
        max_length=20,
        choices=[
            ("goalkeeper", "Goalkeeper"),
            ("defender", "Defender"),
            ("midfielder", "Midfielder"),
            ("forward", "Forward"),
        ],
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="player")

    def __str__(self):
        return f"{self.name} - {self.position}"


# models.py


class Formation(models.Model):
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    players = models.ManyToManyField("Player")

    def __str__(self):
        return f"{self.team.name} Formation"
