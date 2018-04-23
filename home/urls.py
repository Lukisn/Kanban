#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home")
    # TODO: add login, logout, register views
]
