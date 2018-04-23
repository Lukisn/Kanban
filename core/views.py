from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models


def home(request):
    return render(request, "core/home.html", {})


def groups(request):

    return render(request, "core/groups.html", {})


def board_list(request):
    boards = get_list_or_404(models.Board)
    return render(request, "core/board_list.html", {"boards": boards})


def board_details(request, board_id):
    board = get_object_or_404(models.Board, pk=board_id)
    phases = board.phases.all().order_by("order")
    return render(request, "core/board_details.html", {
        "board": board,
        "phases": phases,
    })


def task_list(request):
    tasks = get_list_or_404(models.Task)
    return render(request, "core/task_list.html", {"tasks": tasks})


def task_details(request, task_id):
    task = get_object_or_404(models.Task, pk=task_id)
    return render(request, "core/task_details.html", {"task": task})
