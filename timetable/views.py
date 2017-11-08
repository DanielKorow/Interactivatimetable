from django.shortcuts import render, redirect
from .forms import AuthorizationForm, RegistrationForm
from .scripts import ExtCalendar


def main(request):
    return redirect('/login')


def authorizationband(request):
    auth_form = AuthorizationForm
    reg_form = RegistrationForm
    return render(request, "authorization/auth.html", {"form": auth_form, "reg_form": reg_form})


def schedule(request):
    week = ExtCalendar.week_func()
    monday = week[0]
    tuesday = week[1]
    wednesday = week[2]
    thursday = week[3]
    friday = week[4]
    saturday = week[5]
    sunday = week[6]
    return render(request, "timetable/index.html", {"monday": monday, "tuesday": tuesday, "wednesday": wednesday, "thursday": thursday, "friday": friday, "saturday": saturday, "sunday": sunday})
