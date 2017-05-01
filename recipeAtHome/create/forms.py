from mongodbforms import DocumentForm, EmbeddedDocumentForm, ModelFormOptions
from mongodbforms import IntegerField, BooleanField, CharField
from .models import AmountIngredient, Recipe, RecipeStep, TestModel
from django import forms

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
        fields = ["name", "tags", "description", "ingredients", "steps"]

class SampleForm(DocumentForm):
    document_changed = BooleanField(required=False, widget=forms.HiddenInput())
    append_new_step = BooleanField(required=False, widget=forms.HiddenInput())
    current_id = CharField(required=False, max_length=None, widget=forms.HiddenInput())
    class Meta:
        model = TestModel
        fields = ['name', 'test']
