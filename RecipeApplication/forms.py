from django import forms
from RecipeApplication.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=32)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Такой пользователь существует')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    instructions = forms.CharField(max_length=255)
    cooking_time = forms.IntegerField()
    image = forms.ImageField(upload_to='images', blank=True)
    author = forms.ModelChoiceField(queryset=User.objects.all())
