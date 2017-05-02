from django.shortcuts import render
from django.http import HttpResponse, Http404
import json
# Create your views here.

def index(request):
    data = {'data':'index'}
    return HttpResponse(json.dumps(data), content_type='application/json')

def edit(request, id=None):
    data = {'data':'edit'}
    return HttpResponse(json.dumps(data), content_type='application/json')

def show(request, id=None):
    data = {'data':'show'}
    return HttpResponse(json.dumps(data), content_type='application/json')
