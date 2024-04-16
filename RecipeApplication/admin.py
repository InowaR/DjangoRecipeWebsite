from django.contrib import admin
from RecipeApplication.models import Recipe, Ingredient, RecipeCategory, RecipeCategoryMap, Review


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeCategoryMap)
class RecipeCategoryMapAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
