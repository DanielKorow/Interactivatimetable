from django.shortcuts import render, redirect
from .forms import AuthorizationForm, RegistrationForm


def main(request):
    return redirect('/login')


def authorizationband(request):
    auth_form = AuthorizationForm
    reg_form = RegistrationForm
    return render(request, "authorization/auth.html", {"form": auth_form, "reg_form": reg_form})


def schedule(request):
    return render(request, "timetable/index.html", {})
