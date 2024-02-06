from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from users.views import login


@login_required
def page1(request):
    if request.user.is_authenticated:
        return render(request, "page1.html")
    else:
        return redirect("login")


def games(request):
    return render(request, "games.html")


def teams(request):
    return render(request, "teams.html")


def aboutUs(request):
    return render(request, "aboutUs.html")


def contactUs(request):
    return render(request, "contactUs.html")
