from mongodbforms import DocumentForm, EmbeddedDocumentForm, ModelFormOptions
from .models import Recipe, RecipeStep

class AbstractObjectForm():
    pass

class RecipeForm(DocumentForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'cook_time', 'prep_time', 'ingredients']

class RecipeStepForm(EmbeddedDocumentForm):
    class Meta:
        model=RecipeStep
        fields = ['name','amount']
