from django.urls import path
from .views import (
    HeroesAPIView,
    HeroesListAPIView
)

app_name = "heroes"

urlpatterns = [
    path("list/", HeroesListAPIView.as_view(), name="list"),
    path("<int:pk>", HeroesAPIView.as_view(), name="retrieve")
]
