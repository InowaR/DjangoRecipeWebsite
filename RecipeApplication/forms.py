from django import forms
from RecipeApplication.models import Ingredient


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название')
    description = forms.CharField(max_length=255, label='Описание')
    instructions = forms.CharField(max_length=255, label='Шаги приготовления')
    cooking_time = forms.IntegerField(label='Время приготовления')
    image = forms.ImageField(label='Изображение')
    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(), label='Ингредиенты')

