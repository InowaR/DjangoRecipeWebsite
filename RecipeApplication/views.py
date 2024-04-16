import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from RecipeApplication.forms import LoginForm, RecipeForm
from django.contrib.auth.forms import UserCreationForm
from RecipeApplication.models import Recipe

logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')


@login_required
def index(request):
    logger.info(f"Адрес клиента: {request.META['REMOTE_ADDR']}")
    recipes = Recipe.objects.order_by('?')[:5]
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            instructions = form.cleaned_data['instructions']
            cooking_time = form.cleaned_data['cooking_time']
            image = form.cleaned_data['image']
            ingredients = request.POST.getlist('ingredients')
            author = request.user
            recipe = Recipe.objects.create(title=title, description=description, instructions=instructions,
                                           cooking_time=cooking_time, image=image, author=author)
            for i in ingredients:
                recipe.ingredients.add(i)
            recipe.save()
            return redirect('index')
    else:
        form = RecipeForm()
        context = {
            'form': form
        }
        return render(request, 'create_recipe.html', context)
