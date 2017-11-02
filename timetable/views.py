from django.shortcuts import render, redirect
from .forms import AuthorizationForm


def main(request):
    return redirect('/login')


def authorizationband(request):
    auth_form = AuthorizationForm
    return render(request, "authorization/auth.html", {"form": auth_form})


def schedule(request):
    return render(request, "timetable/index.html", {})
