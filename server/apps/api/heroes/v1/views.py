from rest_framework import views, generics
from .serializers import HeroesAPI
from apps.api.heroes.models import Heroes

class HeroesListAPIView(generics.ListAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesAPI

class HeroesAPIView(generics.RetrieveAPIView):
    serializer_class = HeroesAPI
    queryset = Heroes.objects.all()