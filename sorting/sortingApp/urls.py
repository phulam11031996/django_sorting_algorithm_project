from django.urls import path
from sortingApp.views import HomeView, BubbleView

app_name = 'sortingApp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bubble/', BubbleView.as_view(), name='bubble'),
]
