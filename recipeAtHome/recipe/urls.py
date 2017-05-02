from django.conf.urls import url
from .views import index, edit

urlpatterns = [
    url(r'^$', index),
    url(r'^edit', edit),
]
