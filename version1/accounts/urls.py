# django.contrib.auth import views
import django.contrib.auth.forms
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.user_login, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('register/', views.register, name='register'),
]
