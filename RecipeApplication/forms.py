from django import forms
from django.contrib.auth.models import User


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    instructions = forms.CharField(max_length=255)
    cooking_time = forms.IntegerField()
    image = forms.ImageField()
    author = forms.ModelChoiceField(queryset=User.objects.all())
