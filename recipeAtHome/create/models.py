from mongoengine import Document, DynamicDocument, EmbeddedDocument, fields
from mongoengine import StringField, IntField, FloatField, EmbeddedDocumentListField, EmbeddedDocumentField
# Create your models here.

class IgnoreExtraFields():
    meta = {'strict':False}
    
class AmountIngredient(EmbeddedDocument):
    quantity = FloatField(max_value=100)
    unit = StringField(max_value=100)
    ingredient_name = StringField(max_value=100)

class RecipeStep(EmbeddedDocument):
    ingredients = StringField(max_value=100)
    step_to_perform = StringField(max_value=500)

class Recipe(Document):
    name = StringField(max_length=100)
    tags = StringField(max_length=1000)
    description = StringField(max_length=500)
    ingredients = StringField(max_value=100)
    steps = StringField(max_length=100)    


class TestModel(Document, IgnoreExtraFields):
    name= StringField(max_length=100)
    test = IntField(max_value=9999)
    
