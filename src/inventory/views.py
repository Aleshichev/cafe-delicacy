from django.shortcuts import render
from .models import Ingredients, MenuItems, RecipeRequirements, Purchases
from django.views.generic import ListView
from django.views.generic.edit import CreateView,  DeleteView, UpdateView
from django.views.generic import TemplateView
from .forms import IngredientCreateForm, MenuItemsCreateForm, RecipeRequirementsForm, PurchasesForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum


class HomeView(LoginRequiredMixin, TemplateView):
  template_name = "inventory/home.html"

  def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)
    context = {"name": "vegetable"}
    context["ingredients"] = Ingredients.objects.all()
    context["menu_items"] = MenuItems.objects.all()
    context["purchases"] = Purchases.objects.all()
    return context

# def home(request):
#     context = {"name": "vegetable"}
#     return render(request, "inventory/home.html", context)

class IngredientList(LoginRequiredMixin, ListView):
  model = Ingredients

class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredients
  template_name = 'inventory/ingredient_create_form.html'
  form_class = IngredientCreateForm
#
# class UpdateIngredientView(LoginRequiredMixin, UpdateView):
#   template_name = "inventory/update_ingredient.html"
#   model = Ingredient
#   form_class = IngredientForm

class MenuList(LoginRequiredMixin, ListView):
  model = MenuItems

class MenuCreate(CreateView):
  model = MenuItems
  template_name = 'inventory/ingredient_create_form.html'
  form_class = MenuItemsCreateForm

class RecipeList(LoginRequiredMixin, ListView):
  model = RecipeRequirements

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = RecipeRequirements
  template_name = 'inventory/recipe_create_form.html'
  form_class = RecipeRequirementsForm

class PurchasesList(LoginRequiredMixin, ListView):
  model = Purchases

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["purchases"] = Purchases.objects.all()
    revenue = Purchases.objects.aggregate(revenue=Sum("menuitem__price"))["revenue"]
    total_cost = 0
    for purchase in Purchases.objects.all():
      for recipe_requirement in purchase.menuitem.reciperequirements_set.all():
        total_cost += recipe_requirement.ingredient.unit_price * \
                      recipe_requirement.quantity

    context["revenue"] = revenue
    context["total_cost"] = total_cost
    context["profit"] = revenue - total_cost

    return context

class PurchasesCreate(LoginRequiredMixin, CreateView):
  model = Purchases
  template_name = 'inventory/purschase_create_form.html'
  form_class = PurchasesForm

