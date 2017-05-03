""" Views for Recipe"""
from mongoengine import Document, EmbeddedDocument
from mongoengine import EmbeddedDocumentListField
from mongoengine import StringField, FloatField, ListField
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

class RecipeStep(EmbeddedDocument, DocumentUtils):
    name = StringField(max_length=50)
    amount = StringField(max_length=50)

class Recipe(Document, DocumentUtils):
    title = StringField(max_length=50)
    description = StringField(max_length=None)
    tags = ListField()
    cook_time = FloatField()
    prep_time = FloatField()
    ingredients = StringField()
    steps = EmbeddedDocumentListField(RecipeStep)

    """
/edit/{id} -- edits an existing recipe -IMPLEMENTED
/edit -- creates new recipe -- IMPLEMENTED
/details/{id} -- shows details of a recipe (full view) -- IMPLEMENTED
/edit/{id}/steps/new --Create new ingredient in recipe {id} 
/edit/{id}/steps/{id} -- edits an existing ingredient {id} in recipe{id}
/edit/

    """
