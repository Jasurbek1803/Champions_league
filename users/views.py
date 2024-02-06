from audioop import reverse

from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LogoutView


from users.models import MyUser


def index(request):
    return render(request, "home.html")


def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if MyUser.objects.filter(username=username).exists():
            error_message = (
                "Username already taken. Please choose a different username."
            )
            return render(
                request, "registration.html", {"error_message": error_message}
            )

            # if '' in username or email or password:
            # error_message = 'username, email and password cannot contain spaces. Please enter a valid value.'
            # return render(request, 'registration.html', {'error_message': error_message})

        new_user = MyUser.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        return redirect("login")

    return render(request, "registration.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            request.session["username"] = user.username
            request.session.save()
            return redirect("news")
        else:
            error_message = "Username or password is incorrect."
            return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")
