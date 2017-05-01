"""urls module for create app"""
from django.conf.urls import url
from .views import index, create_recipe_form, new_recipe_form

urlpatterns = [
    url(r'^$', index),
    url(r'^create_recipe', create_recipe_form),
    url(r'^test', new_recipe_form),
]
