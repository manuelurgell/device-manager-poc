from rest_framework import serializers

from devices.models import Device
from devices.serializers import DeviceSerializer
from hubs.models import Hub


class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = ["id", "name", "dwelling"]


class HubCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = ["name"]


class HubListDevicesSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Hub
        fields = ["id", "devices"]


class HubPairDeviceSerializer(serializers.Serializer):
    device_id = serializers.PrimaryKeyRelatedField(queryset=Device.objects.all())
