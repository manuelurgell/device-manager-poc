from rest_framework import serializers

from dwellings.models import Dwelling
from hubs.models import Hub


class DwellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dwelling
        fields = ["id", "name", "occupied"]


class DwellingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dwelling
        fields = ["name"]


class DwellingInstallHubSerializer(serializers.Serializer):
    hub_id = serializers.PrimaryKeyRelatedField(queryset=Hub.objects.all())
