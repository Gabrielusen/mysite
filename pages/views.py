from django.shortcuts import render
from django.views.generic import ListView
from .models import Project


class HomePageView(ListView):
    template_name = 'home.html'
    model = Project
