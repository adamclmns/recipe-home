""" views for managing Recipe Objects """
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core import serializers
from .models import Recipe, RecipeStep, DocumentUtils
from .forms import RecipeForm, RecipeStepForm
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
    objects = Recipe.objects()
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
        obj = DocumentUtils.get_object_or_404(Recipe, id=recipe_id)
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
        object = DocumentUtils.get_object_or_404(Recipe, id=recipe_id)
    else:
        raise Http404
    return render(request, 'details.html', {'data':data, 'object':object})

def delete(request, recipe_id):
    recipe_to_delete = DocumentUtils.get_object_or_404(Recipe, id=recipe_id)
    recipe_to_delete.delete()
    return HttpResponseRedirect('/recipe/')

def edit_recipe_step(request, recipe_id, step_id=None):
    """ /edit/{id}/edit/ /edit/{id}/edit/{id} """
    data = defaultPageInformation()
    data.action = "/recipe/edit/"+recipe_id+"/edit/"
    parent_recipe = DocumentUtils.get_object_or_404(Recipe, id=recipe_id)
    if step_id is None:
        obj = RecipeStep()
    else:
        data.action += step_id
        obj = DocumentUtils.get_object_or_404(RecipeStep, id=step_id)
    if request.method == 'POST':
        form = RecipeStepForm(request.POST, parent_document=parent_recipe, instance=obj  )
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/recipe/details/'+recipe_id)
    else:
        form = RecipeStepForm(parent_document=parent_recipe, instance = obj)
    return render(request, 'edit.html',{'data':data, 'form':form})

