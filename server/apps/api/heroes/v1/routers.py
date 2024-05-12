from django.urls import path
from .views import (
    HeroesAPIView,
    HeroesListAPIView,
    ApplicationListAPIView,
    ApplicationAPIView,
    ApplicationCreateAPIView,
    ArchiveAPIView,
    ArchiveListAPIView
)

app_name = "heroes"

urlpatterns = [
    path("list/", HeroesListAPIView.as_view(), name="list of heroes"),
    path("<int:pk>", HeroesAPIView.as_view(), name="retrieve hero"),
    # path("applications/", ApplicationListAPIView.as_view(), name="list of applications"),
    # path("applications/<int:pk>", ApplicationAPIView.as_view(), name="retrive application"),
    path("applications/create", ApplicationCreateAPIView.as_view(), name="create application"),
    # path("archive/", ArchiveListAPIView.as_view(), name="list of archive"),
    # path("archive/<int:pk>", ArchiveAPIView.as_view(), name="retrieve archive")
]
