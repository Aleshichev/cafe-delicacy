from django.shortcuts import render
from .models import Ingredients
    # MenuItems, RecipeRequirements, Purchases
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


def home(request):
    context = {"name": "vegetable"}
    return render(request, "inventory/home.html", context)

class IngredientList(ListView):
  model = Ingredients