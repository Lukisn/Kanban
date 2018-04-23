# Generated by Django 2.0.4 on 2018-04-23 13:33

import core.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='boards', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='color',
            name='blue',
            field=models.PositiveSmallIntegerField(default=0, validators=[core.models.validate_unsigned_8bit_integer]),
        ),
        migrations.AlterField(
            model_name='color',
            name='green',
            field=models.PositiveSmallIntegerField(default=0, validators=[core.models.validate_unsigned_8bit_integer]),
        ),
        migrations.AlterField(
            model_name='color',
            name='red',
            field=models.PositiveSmallIntegerField(default=0, validators=[core.models.validate_unsigned_8bit_integer]),
        ),
        migrations.AlterField(
            model_name='phase',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
