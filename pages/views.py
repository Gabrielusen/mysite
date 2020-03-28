from django.shortcuts import render
from django.views.generic import TemplateView
import datetime



class HomePageView(TemplateView):
    template_name = 'home.html'
