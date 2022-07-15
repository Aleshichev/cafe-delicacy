from django import forms
from .models import Ingredients, MenuItems

class IngredientCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredients
    fields = ("name", "quantity", "unit_price", "unit")

class MenuItemsCreateForm(forms.ModelForm):
  class Meta:
    model = MenuItems
    fields = ("__all__")
