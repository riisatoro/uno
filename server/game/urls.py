from django.contrib import admin
from django.urls import path, include

from .views import Results

urlpatterns = [
    path('results/', Results.as_view(), name="results")
]
