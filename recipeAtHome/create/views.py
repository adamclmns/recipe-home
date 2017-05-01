from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import RecipeForm, AmountIngredientForm, RecipeStepForm, SampleForm
from .models import Recipe, AmountIngredient, RecipeStep, TestModel
import json

def get_obj_or_404(klass, *args, **kwargs):
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        raise Http404
# Create your views here.
def index(request):
    """
    index page for create recipe app
    """
    return render(request, 'index.html', {'data':''})
    
def create_recipe_form(request):
    """This will bulid the form to create a new car object"""
    print("Create_Recipe Called")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("REQUEST: ", end='')
        print(request)
        # create a form instance and populate it with data from the request:
        form = RecipeForm(request.POST)
        print("FORM: ", end='')
        print(form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            submitted = Recipe.from_json(json.dumps(form.cleaned_data))
            print(submitted.to_json())
            submitted.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/create/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecipeForm()

    return render(request, 'recipeForm.html', {'form': form})


def new_test_old(request):
    # Is there already a Recipe being made? Use query param to get ID of current recipe being edited
    # Populate the already present information
    # Save current information to database if any change
    # Requesting new Embedded Document be added?
    # if yes, generate new Embedded Document Form, add to existing form, and render
    # Completed? Save button?
    data = {}
    data['submitURL'] = '/create/new_test'
    if request.method == 'POST':
        print("REQUEST.POST: ", end='')
        print(request.POST)
        form = SampleForm(request.POST)
        if form.is_valid():
            print("FORM.CLEANED_DATA: ", end='')

            print(form.cleaned_data)
            submitted = TestModel.from_json(json.dumps(form.cleaned_data))
            print('SUBMITTED: ', end='')
            print(submitted.to_json())
            submitted.save()
            return HttpResponseRedirect('/create/new_test')
    else:
        form = SampleForm()
    return render(request, 'testForm.html', {'data':data, 'form':form})

def new_test(request, testId=None):
    if testId == None:
        print("TEST ID IS NONE")
        test_submission = TestModel()
    else:
        print("TEST ID IS NOT NONE")
        test_submission = get_obj_or_404(TestModel, id=testId)
    if request.method == 'POST':
        form = SampleForm(request.POST, instance=test_submission)
        
        if form.is_valid():
            test_submission.pk = None

            test = form.save(commit=False)
            test.id = None
            test.save()

            return HttpResponseRedirect('/create/new_test')
    else:
        form = SampleForm(instance=test_submission)
    return render(request, 'testForm.html', {'form':form})

def list_test(request):
    if request.method == 'GET':
        print("REQUEST.GET")
        tests = [t.to_json() for t in TestModel.objects()]
    return HttpResponse(json.dumps(tests), content_type='application/json')
