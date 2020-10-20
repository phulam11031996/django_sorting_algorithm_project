from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'sortingApp/home.html'

class BubbleView(TemplateView):
    template_name = 'sortingApp/bubble.html'
