from django.urls import path
from . import views


urlpatterns = [
  path('', views.HomeView.as_view(), name="home"),
  path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist"),
  path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
  path("menu/list", views.MenuList.as_view(), name="menulist"),
  path("menu/create", views.MenuCreate.as_view(), name="menucreate"),
  path("recipe/list", views.RecipeList.as_view(), name="recipelist"),
  path("recipe/create", views.RecipeCreate.as_view(), name="recipecreate"),
  path("purchas/list", views.PurchasesList.as_view(), name="purchaslist"),
  path("purchas/create", views.PurchasesCreate.as_view(), name="purchascreate"),
  path('reports', views.ReportView.as_view(), name="reports")
]