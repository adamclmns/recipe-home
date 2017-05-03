from django.conf.urls import url
from .views import index, edit, delete, details, edit_recipe_step

urlpatterns = [
    url(r'^edit/(?P<recipe_id>\w+)/edit/(?P<step_id>\w+)', edit_recipe_step),
    url(r'^edit/(?P<recipe_id>\w+)/edit', edit_recipe_step),
    url(r'^delete/(?P<recipe_id>\w+)', delete),
    url(r'^details/(?P<recipe_id>\w+)', details),
    url(r'^edit/(?P<recipe_id>\w+)', edit),
    url(r'^edit/', edit),
    url(r'^$', index),
]
