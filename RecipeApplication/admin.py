from django.contrib import admin
from RecipeApplication.models import User, Recipe, Ingredient, RecipeCategory, RecipeCategoryMap


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeCategoryMap)
class RecipeCategoryMapAdmin(admin.ModelAdmin):
    pass
