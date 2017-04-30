from mongodbforms import DocumentForm, EmbeddedDocumentForm, ModelFormOptions
from mongodbforms import IntegerField, BooleanField
from .models import AmountIngredient, Recipe, RecipeStep


class AmountIngredientForm(EmbeddedDocumentForm):
    class Meta:
        model = AmountIngredient
        embedded_field_name="Ingredient & Amount"
        fields = ['quantity','unit','ingredient_name']

class RecipeStepForm(EmbeddedDocumentForm):
    class Meta:
        model = RecipeStep
        embedded_field_name = "recipe_step"
        fields = ["ingredients","step_to_perform"]

class RecipeForm(DocumentForm):
    add_step = BooleanField()
    class Meta:
        model = Recipe
        embedded_field_name = "recipe"
        fields = ["name","tags","description"]
