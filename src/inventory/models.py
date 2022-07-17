import datetime

from django.db import models

# Create your models here.

# An inventory of different Ingredients, their available quantity, and their prices per unit
class Ingredients(models.Model):
  name = models.CharField(max_length=200, unique=True)
  quantity = models.FloatField(default=0)
  unit = models.CharField(max_length=20)
  unit_price = models.FloatField(default=0)

  def get_absolute_url(self):
    return "list"

  def __str__(self):
    return f"{self.name} - {self.quantity} - {self.unit} - {self.unit_price}."

# # A list of the restaurant’s MenuItems, and the price set for each entry


class MenuItems(models.Model):
  titel = models.CharField(max_length=200, unique=True)
  price = models.FloatField(default=0)

  def get_absolute_url(self):
    return "list"

  def available(self):
    return all(X.enough() for X in self.reciperequirements_set.all())

  def __str__(self):
    return f"{self.titel} - {self.price}$"

# # A list of the ingredients that each menu item requires (RecipeRequirements)


class RecipeRequirements(models.Model):
  menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
  quantity = models.FloatField(default=0)

  def get_absolute_url(self):
    return "list"

  def enough(self):
      return self.quantity <= self.ingredient.quantity

  def __str__(self):
    return f"{self.menuitem}"
# # A log of all Purchases made at the restaurant
#
class Purchases(models.Model):
  menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(default=datetime.date.today)

  def get_absolute_url(self):
    return "list"

  def __str__(self):
    return f"{self.menuitem}"

