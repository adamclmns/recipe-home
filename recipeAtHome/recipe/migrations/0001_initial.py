# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('cook_time', models.FloatField()),
                ('prep_time', models.FloatField()),
                ('ingredients', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.ManyToManyField(to='recipe.RecipeStep'),
        ),
    ]
