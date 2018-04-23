#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = "core"
urlpatterns = [
    path("home", views.home, name="home"),
    path("groups", views.groups, name="groups"),
    path("boards", views.boards, name="boards"),
    path("tasks", views.tasks, name="tasks"),
]
