"""urls module for create app"""
from django.conf.urls import url
from .views import index, create_recipe_form, new_test, list_test

urlpatterns = [
    url(r'^$', index),
    url(r'^create_recipe', create_recipe_form),
    url(r'^new_test/(?P<testId>\w+)/$', new_test),
]
