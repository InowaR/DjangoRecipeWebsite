from django import forms
from RecipeApplication.models import Ingredient


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    instructions = forms.CharField(max_length=255)
    cooking_time = forms.IntegerField()
    image = forms.ImageField()
    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())
