import datetime

from django.db import models

# Create your models here.

# An inventory of different Ingredients, their available quantity, and their prices per unit
class Ingredients(models.Model):
  name = models.CharField(max_length=200)
  quantity = models.FloatField(default=0)
  unit = models.CharField(max_length=20)
  unit_price = models.FloatField(default=0)

  def get_absolute_url(self):
    return "list"

# # A list of the restaurant’s MenuItems, and the price set for each entry
#
class MenuItems(models.Model):
  titel = models.CharField(max_length=200)
  price = models.FloatField(default=0)

  def get_absolute_url(self):
    return "list"

# # A list of the ingredients that each menu item requires (RecipeRequirements)
#
class RecipeRequirements(models.Model):
  menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
  quantity = models.FloatField(default=0)
# # A log of all Purchases made at the restaurant
#
class Purchases(models.Model):
  menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(default=datetime.date.today)

