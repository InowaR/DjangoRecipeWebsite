from django import forms
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from RecipeApplication.forms import LoginForm


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user:
                login(request, user)
            else:
                raise forms.ValidationError('Неверные имя пользователя или пароль')
            return redirect('index')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def index(request):
    return render(request, 'index.html')
