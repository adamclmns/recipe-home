"""urls module for create app"""
from django.conf.urls import url
from create.views import index, create_recipe_form

urlpatterns = [
    url(r'^$', index),
    url(r'^create_recipe', create_recipe_form),
]
