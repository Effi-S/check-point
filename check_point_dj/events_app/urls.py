
from django.urls import path
from .views import post, get_stats
urlpatterns = [
    path('events', post),
    path('stats', get_stats)
]
