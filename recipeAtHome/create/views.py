from django.shortcuts import render
from .forms import RecipeForm, AmountIngredientForm, RecipeStepForm
from .models import Recipe, AmountIngredient, RecipeStep


# Create your views here.
def index(request):
    """
    index page for create recipe app
    """
    return render(request, 'index.html', {'data':''})
    
def create_recipe_form(request):
    print("Create_Recipe Called")
    """This will bulid the form to create a new car object"""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request)
        # create a form instance and populate it with data from the request:
        form = RecipeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            submitted = Recipe.from_json(json.dumps(form.cleaned_data))
            print(submitted)
            submitted.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/create/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecipeForm()

    return render(request, 'recipeForm.html', {'form': form})
