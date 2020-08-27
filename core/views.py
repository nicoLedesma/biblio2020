from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import MateriaLectura

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/home.html'

