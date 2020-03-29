from django.shortcuts import render
from django.views.generic import TemplateView
import datetime


now = datetime.datetime.now()


class HomePageView(TemplateView):
    template_name = 'home.html'
