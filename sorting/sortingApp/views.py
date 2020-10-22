from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'sortingApp/home.html'

class BubbleView(TemplateView):
    template_name = 'sortingApp/bubble.html'

class SelectionView(TemplateView):
    template_name = 'sortingApp/selection.html'

class InsertionView(TemplateView):
    template_name = 'sortingApp/insertion.html'

class MergeView(TemplateView):
    template_name = 'sortingApp/merge.html'

class QuickView(TemplateView):
    template_name = 'sortingApp/quick.html'

class RadixView(TemplateView):
    template_name = 'sortingApp/radix.html'
