from django.shortcuts import render
from .models import Ingredients, MenuItems, RecipeRequirements, Purchases
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import IngredientCreateForm, MenuItemsCreateForm, RecipeRequirementsForm, PurchasesForm
# Create your views here.


def home(request):
    context = {"name": "vegetable"}
    return render(request, "inventory/home.html", context)

class IngredientList(ListView):
  model = Ingredients

class IngredientCreate(CreateView):
  model = Ingredients
  template_name = 'inventory/ingredient_create_form.html'
  form_class = IngredientCreateForm

class MenuList(ListView):
  model = MenuItems

class MenuCreate(CreateView):
  model = MenuItems
  template_name = 'inventory/ingredient_create_form.html'
  form_class = MenuItemsCreateForm

class RecipeList(ListView):
  model = RecipeRequirements

class RecipeCreate(CreateView):
  model = RecipeRequirements
  template_name = 'inventory/recipe_create_form.html'
  form_class = RecipeRequirementsForm

class PurchasesList(ListView):
  model = Purchases

class PurchasesCreate(CreateView):
  model = Purchases
  template_name = 'inventory/purschase_create_form.html'
  form_class = PurchasesForm