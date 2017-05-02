from mongoengine import Document, EmbeddedDocumentField, EmbeddedDocumentListField
from mongoengine import StringField, IntField, FloatField, DateTimeField
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

class Recipe(Document, DocumentUtils):
    title = StringField(max_length=50)
    description = StringField(max_length=None)
    cook_time = FloatField()
    prep_time = FloatField()
    ingredients = StringField()
    steps = StringField()
