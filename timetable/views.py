from django.shortcuts import render, redirect
from .forms import AuthorizationForm


def main(request):
    return redirect('/login')


def AuthorizationBand(request):
    auth_form = AuthorizationForm
    return render(request, "authorization/auth.html", {"form": auth_form})
