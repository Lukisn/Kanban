from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


def deleted_user():
    """Function returning or creating a sentinel user object."""
    return get_user_model().objects.get_or_create(username="deleted")[0]


class Board(models.Model):
    # required fields:
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET(deleted_user),
                                related_name="boards_created")
    # optional fields:
    members = models.ManyToManyField(User, related_name="boards", blank=True)

    def __str__(self):
        return self.name


class Phase(models.Model):
    # required fields:
    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)
    board = models.ForeignKey(Board, on_delete=models.CASCADE,
                              related_name="phases")
    # no optional fields

    def __str__(self):
        return self.name


def validate_unsigned_8bit_integer(value):
    """Vaidation function for 8-bit unsigned integers."""
    if not 0 <= value <= 255:
        raise ValidationError(f"{value} is not a valid unsigned 8-bit integer")


class Color(models.Model):
    # required fields:
    name = models.CharField(max_length=100)
    red = models.PositiveSmallIntegerField(default=0,
        validators=[validate_unsigned_8bit_integer])
    green = models.PositiveSmallIntegerField(default=0,
        validators=[validate_unsigned_8bit_integer])
    blue = models.PositiveSmallIntegerField(default=0,
        validators=[validate_unsigned_8bit_integer])
    # no optional fields

    def __str__(self):
        return self.name


class Status(models.Model):
    # required fields:
    name = models.CharField(max_length=100)
    description = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE,
                              related_name="states")
    # optional fields:
    color = models.ForeignKey(Color, on_delete=models.CASCADE,
                              related_name="+", null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    # required fields:
    name = models.CharField(max_length=100)
    description = models.TextField()
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE,
                              related_name="tasks")
    status = models.ForeignKey(Status, on_delete=models.CASCADE,
                               related_name="tasks")
    # optional fields:
    creation_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET(deleted_user),
                                related_name="tasks_created")
    due_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)
    editor = models.ForeignKey(User, on_delete=models.SET(deleted_user),
                               related_name="tasks_edited", null=True,
                               blank=True)
    assigned_to = models.ManyToManyField(User, related_name="tasks_assigned",
                                         blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    # required fields:
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET(deleted_user),
                                related_name="comments_created")
    # no optional fields

    def __str__(self):
        return self.text
