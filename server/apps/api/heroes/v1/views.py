from rest_framework import views, generics
from .serializers import (
    HeroesAPI,
    ApplicationAPI,
    ArchiveAPI
)
from apps.api.heroes.models import (
    Heroes,
    Application,
    Archive
)

class HeroesListAPIView(generics.ListAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesAPI

class HeroesAPIView(generics.RetrieveAPIView):
    serializer_class = HeroesAPI
    queryset = Heroes.objects.all()

class ApplicationListAPIView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationAPI

class ApplicationAPIView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationAPI
class ApplicationCreateAPIView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationAPI

class ArchiveListAPIView(generics.ListAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveAPI

class ArchiveAPIView(generics.RetrieveAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveAPI
