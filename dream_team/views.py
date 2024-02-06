# dream_team/views.py
from django.shortcuts import render, redirect

from .forms import TeamForm, PlayerForm

from .models import Team, Player, Formation


def dream_team(request):
    if request.method == "POST":
        team_name = request.POST.get("team_name")
        user = request.user
        new_team, created = Team.objects.get_or_create(name=team_name, users=user)

        return redirect("add_players", team_id=new_team.id)

    return render(request, "dream_team.html", {"user": request.user})


def add_players(request, team_id):
    team = Team.objects.get(pk=team_id)
    max_players = 11
    max_goalkeepers = 1
    if Player.objects.filter(team=team).count() >= max_players:

        return redirect("full_formation", team_id=team_id)

    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data["name"]
            position = form.cleaned_data["position"]

            # Check if the player name is unique within the team
            if Player.objects.filter(team=team, name=player_name).exists():
                form.add_error(
                    "name", "Player with this name already exists in the team."
                )
            else:
                # Check the number of goalkeepers
                if (
                    position == "goalkeeper"
                    and Player.objects.filter(team=team, position="goalkeeper").count()
                    >= max_goalkeepers
                ):
                    form.add_error(
                        "position", "You can only have one goalkeeper in the team."
                    )
                else:
                    player = form.save(commit=False)
                    player.team = team
                    player.save()

                    # Check the number of players after adding one
                    if Player.objects.filter(team=team).count() >= max_players:
                        # If the team now has the maximum number of players, redirect to the formation view
                        return redirect("full_formation", team_id=team_id)
                    else:
                        # Otherwise, stay on the add_players view
                        return redirect("add_players", team_id=team_id)
    else:
        form = PlayerForm()

    players = Player.objects.filter(team=team)
    player_count = players.count()  # Count of players
    return render(
        request,
        "add_player.html",
        {
            "form": form,
            "team": team,
            "players": players,
            "player_count": player_count,
            "user": request.user,
        },
    )


def full_formation(request, team_id):
    team = Team.objects.get(pk=team_id)
    players = Player.objects.filter(team=team)

    # Dictionary to store players by position
    formation = {
        "goalkeeper": [],
        "defender": [],
        "midfielder": [],
        "forward": [],
    }

    # Categorize players by position
    for player in players:
        formation[player.position].append(player)

    return render(
        request,
        "full_formation.html",
        {"team": team, "formation": formation, "user": request.user},
    )
