from django.shortcuts import render, redirect
from .forms import AuthorizationForm, RegistrationForm, CreateRep
from .scripts import ExtCalendar


def main(request):
    return redirect('/login')


def authorizationband(request):
    auth_form = AuthorizationForm
    reg_form = RegistrationForm(request.POST)
    if reg_form.is_valid():
        reg_form.save()
        redirect("/schedule")
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


def create_rep(request):
    create_form = CreateRep(request.POST)
    if create_form.is_valid():
        start = create_form.cleaned_data['time_start']
        end = create_form.cleaned_data['time_end']
        print(start + " " + end)
        create_form.save()
    return render(request, "timetable/create_rep.html", {"create": create_form})