from django.db import models

# Create your models here.

# An inventory of different Ingredients, their available quantity, and their prices per unit
class Ingredients(models.Model):
  name = models.CharField(max_length=200)
  quantity = models.IntegerField(default=0)
  price = models.IntegerField(default=0)

# A list of the ingredients that each menu item requires (RecipeRequirements)

class RecipeRequirements(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField(default=0)
  ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)

# A list of the restaurant’s MenuItems, and the price set for each entry

class MenuItems(models.Model):
  name_item = models.CharField(max_length=200)
  reciperequirements = models.ForeignKey(RecipeRequirements, on_delete=models.CASCADE)

# A log of all Purchases made at the restaurant
class Purchases(models.Model):
  name = models.CharField(max_length=200)
  date = models.DateField()
  price = models.IntegerField(default=0)
  menuitems = models.ForeignKey(MenuItems, on_delete=models.CASCADE)