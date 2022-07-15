from django import forms
from .models import Ingredients, MenuItems, RecipeRequirements, Purchases

class IngredientCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredients
    fields = ("name", "quantity", "unit_price", "unit")

class MenuItemsCreateForm(forms.ModelForm):
  class Meta:
    model = MenuItems
    fields = ("__all__")

class RecipeRequirementsForm(forms.ModelForm):
  class Meta:
    model = RecipeRequirements
    fields = ("__all__")

class PurchasesForm(forms.ModelForm):
  class Meta:
    model = Purchases
    fields = ("__all__")

