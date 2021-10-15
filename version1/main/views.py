from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *


def index(request):
    data = {
        'title': 'Главная страница'
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
