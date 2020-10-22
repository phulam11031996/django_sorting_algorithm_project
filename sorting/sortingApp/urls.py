from django.urls import path
from sortingApp.views import HomeView, BubbleView, SelectionView, InsertionView, MergeView, QuickView, RadixView
app_name = 'sortingApp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bubble/', BubbleView.as_view(), name='bubble'),
    path('insertion/', InsertionView.as_view(), name='insertion'),
    path('selection/', SelectionView.as_view(), name='selection'),
    path('merge/', MergeView.as_view(), name='merge'),
    path('quick/', QuickView.as_view(), name='quick'),
    path('radix/', RadixView.as_view(), name='radix'),
]
