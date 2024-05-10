from rest_framework import serializers
from apps.api.heroes.models import (
    Heroes,
    Application,
    Archive
)


class HeroesAPI(serializers.ModelSerializer):

    class Meta:
        model = Heroes
        fields = "__all__"

class ApplicationAPI(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = "__all__"

class ArchiveAPI(serializers.ModelSerializer):

    class Meta:
        model = Archive
        fields = "__all__"