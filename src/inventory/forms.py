from django import forms
from .models import Ingredients

class IngredientCreateForm(forms.ModelForm):
  class Meta:
    model = Ingredients
    fields = ("name", "quantity", "unit_price", "unit")