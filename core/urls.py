#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = "core"
urlpatterns = [
    path("home", views.home, name="home"),
    path("groups", views.groups, name="groups"),

    path("boards", views.board_list, name="board_list"),
    path("board/<int:board_id>", views.board_details, name="board_details"),

    path("tasks", views.task_list, name="task_list"),
    path("task/<int:task_id>", views.task_details, name="task_details"),
]
