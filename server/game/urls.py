from django.contrib import admin
from django.urls import path, include

from .views import (
    ResultsView,
    RoomsView,
    PlayerLeaveView,
)

urlpatterns = [
    path('rooms/', RoomsView.as_view(), name="rooms"),
    path('rooms/leave/', PlayerLeaveView.as_view(), name="left_game"),
    path('results/', ResultsView.as_view(), name="results"),
]
