from rest_framework import serializers
from apps.api.heroes.models import Heroes


class HeroesAPI(serializers.ModelSerializer):

    class Meta:
        model = Heroes
        fields = "__all__"
