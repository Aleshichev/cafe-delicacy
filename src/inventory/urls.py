from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name="home"),
  path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist"),
  path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
  path("menu/list", views.MenuList.as_view(), name="menulist"),
  path("menu/create", views.MenuCreate.as_view(), name="menucreate"),
]