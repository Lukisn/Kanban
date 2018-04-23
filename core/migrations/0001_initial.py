# Generated by Django 2.0.4 on 2018-04-23 13:26

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=models.SET(core.models.deleted_user), related_name='boards_created', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('red', models.PositiveSmallIntegerField(validators=[core.models.validate_unsigned_8bit_integer])),
                ('green', models.PositiveSmallIntegerField(validators=[core.models.validate_unsigned_8bit_integer])),
                ('blue', models.PositiveSmallIntegerField(validators=[core.models.validate_unsigned_8bit_integer])),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=models.SET(core.models.deleted_user), related_name='comments_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('order', models.SmallIntegerField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phases', to='core.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='core.Board')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
                ('assigned_to', models.ManyToManyField(blank=True, related_name='tasks_assigned', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=models.SET(core.models.deleted_user), related_name='tasks_created', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=models.SET(core.models.deleted_user), related_name='tasks_edited', to=settings.AUTH_USER_MODEL)),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.Phase')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.Status')),
            ],
        ),
    ]
