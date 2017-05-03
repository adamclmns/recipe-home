""" Views for Recipe"""
from django.db import models
from django.http import Http404
from django.forms import ModelForm

class IngredientValue(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    amount = models.FloatField()

class IngredientValueForm(ModelForm):
    class Meta:
        model=IngredientValue
        fields = ['name','unit','amount']

class RecipeStep(models.Model):
    ingredients = models.ManyToManyField(IngredientValue)
    instructions = models.CharField(max_length=500, default=None, blank=True)


class RecipeStepForm(ModelForm):
    class Meta:
        model=RecipeStep
        fields = ['instructions']

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    cook_time = models.FloatField()
    prep_time = models.FloatField()
    steps = models.ManyToManyField(RecipeStep)

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cook_time', 'prep_time']
