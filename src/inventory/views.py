from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import Ingredients, MenuItems, RecipeRequirements, Purchases
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from .forms import IngredientCreateForm, MenuItemsCreateForm, RecipeRequirementsForm, PurchasesForm, RegisterUserForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy


class HomeView(LoginRequiredMixin, TemplateView):
  template_name = "inventory/home.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
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

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
  template_name = "inventory/update_ingredient.html"
  model = Ingredients
  form_class = IngredientCreateForm

  def get_success_url(self):
    return reverse_lazy('ingredientlist')


class DeleteIngredientView(LoginRequiredMixin, DeleteView):
  model = Ingredients
  template_name = 'inventory/delete_ingr.html'
  success_url = reverse_lazy('ingredientlist')


class MenuList(LoginRequiredMixin, ListView):
  model = MenuItems

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["menu_items"] = MenuItems.objects.all()
    return context

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

class RegisterUser(CreateView):
  form_class = RegisterUserForm
  success_url = reverse_lazy("login")
  template_name = "registration/sign_up.html"

  def form_valid(self, form):
    """автоматически возвращает на главную страницу"""
    user = form.save()
    login(self.request, user)
    return redirect('home')

class LoginUser(LoginView):
  form_class = AuthenticationForm
  template_name = "registration/login.html"

  def get_success_url(self):
    return reverse_lazy('home')

def log_out(request):
  logout(request)
  return redirect("home")




