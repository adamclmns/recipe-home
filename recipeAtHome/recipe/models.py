""" Views for Recipe"""
from django.db import models
from django.http import Http404

# Create your models here.
class DocumentUtils():
    meta = {'strict':False}
    @staticmethod
    def get_object_or_404(klass, *args, **kwargs):
        try:
            return klass.objects.get(*args, **kwargs)
        except klass.DoesNotExist:
            raise Http404

class RecipeStep(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    cook_time = models.FloatField()
    prep_time = models.FloatField()
    ingredients = models.CharField(max_length=50)
    steps = models.ManyToManyField(RecipeStep)

    """
/edit/{id} -- edits an existing recipe -IMPLEMENTED
/edit -- creates new recipe -- IMPLEMENTED
/details/{id} -- shows details of a recipe (full view) -- IMPLEMENTED
/edit/{id}/steps/new --Create new ingredient in recipe {id} 
/edit/{id}/steps/{id} -- edits an existing ingredient {id} in recipe{id}
/edit/

    """
