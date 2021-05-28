from django.contrib import admin
from django.urls import path, include

from .views import (
    ResultsView,
    GameView,
)

urlpatterns = [
    path('rooms/', GameView.as_view(), name="games"),
    path('results/', ResultsView.as_view(), name="results"),
]
