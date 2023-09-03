from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course

# Create your views here.
class HomeView(TemplateView):
    template_name='search.html'
    
