from django.conf.urls import url
from .views import index, edit, delete, details, edit_recipe_step, delete_step, add_ingredient, delete_ingredient

urlpatterns = [
    url(r'^edit/(?P<recipe_id>\w+)/edit/(?P<step_id>\w+)', edit_recipe_step),
    url(r'^details/(?P<recipe_id>\w+)/delete/(?P<step_id>\w+)', delete_step),
    url(r'^details/(?P<recipe_id>\w+)/step/(?P<step_id>\w+)/delete/(?P<ingredient_id>\w+)', delete_ingredient),
    url(r'^details/(?P<recipe_id>\w+)/add_ingredient/(?P<step_id>\w+)', add_ingredient),
    url(r'^edit/(?P<recipe_id>\w+)/edit', edit_recipe_step),
    url(r'^delete/(?P<recipe_id>\w+)', delete),
    url(r'^details/(?P<recipe_id>\w+)', details),
    url(r'^edit/(?P<recipe_id>\w+)', edit),
    url(r'^edit/', edit),
    url(r'^$', index),
]
