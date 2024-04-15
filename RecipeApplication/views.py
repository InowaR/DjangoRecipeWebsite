import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from RecipeApplication.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm

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
    return render(request, 'index.html')
