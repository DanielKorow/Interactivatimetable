from django.shortcuts import render, redirect


def main(request):
    return redirect('/login')


def AuthorizationBand(request):
    return render(request, "authorization/auth.html", {})