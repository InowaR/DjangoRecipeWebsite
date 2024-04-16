from django.contrib.auth import get_user_model
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RecipeCategoryMap(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recipe.title}, {self.category.name}'


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating}, {self.author.name}, {self.recipe.title}'
