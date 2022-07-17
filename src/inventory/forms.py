from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class RegisterUserForm(UserCreationForm):
  username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
  password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
  password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-input'}),
      'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
      'password2': forms.PasswordInput(attrs={'class': 'form-input'})
    }


