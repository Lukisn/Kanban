from django.shortcuts import render


def index(request):
    return render(request, "home/index.html", context={})


def login(request):
    return render(request, "home/login.html", context={})


def signup(request):
    return render(request, "home/signup.html", context={})
