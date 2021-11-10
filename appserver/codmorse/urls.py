from django.urls import path
from .views import CodMorseViewSet

urlpatterns = [
    path('morse/', CodMorseViewSet.as_view())
]