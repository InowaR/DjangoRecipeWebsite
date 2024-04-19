import uvicorn
from fastapi import HTTPException
from DjangoRecipeWebsite.asgi import app
from RecipeApplication.models import Recipe, Ingredient


@app.get("/recipes/")
def get_all_recipes():
    return [recipe for recipe in Recipe.objects.all()]


@app.get("/recipes/{recipe_name}")
def get_recipe_by_name(recipe_name: str):
    recipe = Recipe.objects.filter(title=recipe_name).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Рецепт не найден.")
    return recipe


@app.get("/recipes/ingredients/{ingredient_name}")
def get_recipes_by_ingredient(ingredient_name: str):
    ingredient = Ingredient.objects.filter(name=ingredient_name).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ингредиент не найден.")
    recipes = Recipe.objects.filter(ingredients__in=[ingredient]).all()
    return [recipe for recipe in recipes]


@app.get("/ingredients/")
def get_ingredients():
    return [ingredient for ingredient in Ingredient.objects.all()]


@app.post("/ingredients/")
def create_ingredient(ingredient_name: str):
    existing_ingredient = Ingredient.objects.filter(name=ingredient_name).first()
    if existing_ingredient:
        raise HTTPException(status_code=400, detail="Ингредиент с таким названием уже существует.")
    new_ingredient = Ingredient.objects.create(name=ingredient_name)
    new_ingredient.save()
    return new_ingredient


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
