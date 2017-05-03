from django.forms import ModelForm 
from .models import Recipe, RecipeStep

class AbstractObjectForm():
    pass

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cook_time', 'prep_time', 'ingredients']

class RecipeStepForm(ModelForm):
    class Meta:
        model=RecipeStep
        fields = ['name','amount']
