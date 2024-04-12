from django.shortcuts import render

from RecipeApplication.forms import RegistrationForm
from RecipeApplication.models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            User.create_new_user(username, password)
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)



def index(request):
    return render(request, 'index.html')
