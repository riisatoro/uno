from django.contrib import admin
from django.urls import path, include

from .views import (
    ResultsView,
    GameView,
    MyGame,
)

urlpatterns = [
    path('rooms/', GameView.as_view(), name="games"),
    path('rooms/my/', MyGame.as_view(), name="my_games"),
    path('results/', ResultsView.as_view(), name="results"),
]
