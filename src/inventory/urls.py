from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
  path("logout/", views.log_out, name="logout"),
  path('accounts/login/', views.LoginUser.as_view(), name="login"),
  path("signup/", views.RegisterUser.as_view(), name="signup"),
  path('', views.HomeView.as_view(), name="home"),
  path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist"),
  path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
  path('ingredient/<slug:pk>/update', views.UpdateIngredientView.as_view(), name="update_ingredient"),
  path("ingredient/<slug:pk>/delete", views.DeleteIngredientView.as_view(), name="ingredientdelete"),
  path('recipe/<slug:pk>/update', views.UpdateRecipeView.as_view(), name="update_recipe"),
  path("recipe/<slug:pk>/delete", views.DeleteRecipeView.as_view(), name="recipedelete"),
  path("menu/list", views.MenuList.as_view(), name="menulist"),
  path("menu/create", views.MenuCreate.as_view(), name="menucreate"),
  path("recipe/list", views.RecipeList.as_view(), name="recipelist"),
  path("recipe/create", views.RecipeCreate.as_view(), name="recipecreate"),
  path("purchas/list", views.PurchasesList.as_view(), name="purchaslist"),
  path("purchas/create", views.PurchasesCreate.as_view(), name="purchascreate"),
]