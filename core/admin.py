from django.contrib import admin
from . import models


class BoardAdmin(admin.ModelAdmin):
    model = models.Board


admin.site.register(models.Board)
admin.site.register(models.Phase)
admin.site.register(models.Color)
admin.site.register(models.Status)
admin.site.register(models.Task)
admin.site.register(models.Comment)
