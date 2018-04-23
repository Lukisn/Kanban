from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "core/home.html", {})


def groups(request):
    return render(request, "core/groups.html", {})


def boards(request):
    return render(request, "core/boards.html", {})


def tasks(request):
    return render(request, "core/tasks.html", {})
