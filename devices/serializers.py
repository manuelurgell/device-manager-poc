from rest_framework import serializers

from devices.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["id", "type", "state", "paired", "hub"]


class DeviceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["type", "state"]


class DeviceStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["state"]
