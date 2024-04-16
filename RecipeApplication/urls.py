from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
]
