from mongodbforms import DocumentForm, EmbeddedDocumentForm, ModelFormOptions
from .models import Recipe

class AbstractObjectForm():
    pass

class RecipeForm(DocumentForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cook_time', 'prep_time', 'ingredients', 'steps']
