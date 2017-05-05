""" views for managing Recipe Objects """
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core import serializers
from .models import Recipe, RecipeStep, Ingredient
from .models import RecipeForm, RecipeStepForm, IngredientForm
import json

class defaultPageInformation(object):
    """This is for Convinience, a page data element that can be used to populate templates. """
    def __init__(self):
        self.action = ""
        self.title = "DEFAULT TITLE"

def index(request):
    """ / """
    data = defaultPageInformation()
    data.action = "TEST"
    objects = Recipe.objects.all()
    return render(request, 'index.html', {'data':data, 'objects':objects})

def edit(request, recipe_id=None):
    """ /edit /edit/{id} """
    data = defaultPageInformation()
    data.action = "/recipe/edit/"
    if recipe_id is None:
        obj = Recipe()
    else:
        # If we have an ID, we want to be sure to POST back to that same ID in the url, 
        # else it makes a new one
        data.action += recipe_id
        obj = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST or None, instance=obj)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/recipe/')
    else:
        form = RecipeForm(instance=obj)
    return render(request, 'edit.html', {'data':data, 'form':form})

def details(request, recipe_id=None):
    """ /details/{id} """
    data = defaultPageInformation()
    if recipe_id != None:
        object = get_object_or_404(Recipe, id=recipe_id)
    else:
        raise Http404
    return render(request, 'details.html', {'data':data, 'object':object})

def delete(request, recipe_id):
    recipe_to_delete = get_object_or_404(Recipe, id=recipe_id)
    recipe_to_delete.delete()
    print("DELETED - $s" %recipe_id)
    return HttpResponseRedirect('/recipe/')

def delete_step(request, recipe_id, step_id):
    recipe_step_to_delete = get_object_or_404(RecipeStep, id=step_id)
    recipe_step_to_delete.delete()
    print("DLETED STEP %s" %step_id)
    return HttpResponseRedirect('/recipe/details/'+recipe_id)

def edit_recipe_step(request, recipe_id, step_id=None):
    """ /edit/{id}/edit/{id} /edit/{id}/edit """
    data = defaultPageInformation()
    data.action = "/recipe/edit/"+recipe_id+"/edit"
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if step_id is None:
        recipe_step = RecipeStep()
        print("Step ID Is None")
    else:
        # If we have an ID, we want to be sure to POST back to that same ID in the url
        # else it makes a new one
        print("Step ID Is Not Null")
        data.action += "/" + step_id
        recipe_step = get_object_or_404(RecipeStep, id=step_id)
    if request.method == 'POST':
        form = RecipeStepForm(request.POST, instance=recipe_step)
        if form.is_valid():
            recipe_step = form.save()
            print("adding the step to the recipe")
            recipe.steps.add(recipe_step)
            return HttpResponseRedirect('/recipe/details/'+recipe_id)
    else:
        form = RecipeStepForm(instance=recipe_step)
    return render(request, 'edit.html', {'data':data, 'form':form})


def add_ingredient(request, recipe_id, step_id):
    data = defaultPageInformation()
    data.action = "/recipe/details/"+recipe_id+"/add_ingredient/"+step_id
    # 404 if this isn't a valid recipe
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe_step = get_object_or_404(RecipeStep, id=step_id)
    
    ingredient = Ingredient()
    
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save()
            print("adding the ingredient to the recipe_step")
            recipe_step.ingredients.add(ingredient)
            return HttpResponseRedirect('/recipe/details/'+recipe_id)
    else:
        form = IngredientForm()
    return render(request, 'edit.html', {'data':data, 'form':form})

def delete_ingredient(request, recipe_id, step_id, ingredient_id):
    ingredient_to_delete = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient_to_delete.delete()
    print("DELETED INGREDIENT ID %s" %ingredient_id)
    return HttpResponseRedirect("/recipe/details/"+recipe_id)