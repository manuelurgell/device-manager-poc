from rest_framework.decorators import action
from rest_framework.response import Response

from app.urls import router
from devices.exceptions import DeviceAlreadyPairedError
from devices.models import Device
from hubs import serializers
from hubs.models import Hub
from utils.mixins import (
    BaseGenericViewSet,
    CreateModelMixin,
    ListModelMixin,
)


class HubViewSet(
    ListModelMixin,
    CreateModelMixin,
    BaseGenericViewSet,
):

    queryset = Hub.objects.all()

    list_serializer_class = serializers.HubSerializer
    create_serializer_class = serializers.HubCreateSerializer

    pair_device_serializer_class = serializers.HubPairDeviceSerializer
    list_devices_serializer_class = serializers.HubListDevicesSerializer

    @action(detail=True, methods=["post"], url_path="pair-device")
    def pair_device(self, request, pk: int):
        hub: Hub = self.get_object()

        serializer = self.get_serializer(data=request.data, action="pair_device")
        serializer.is_valid(raise_exception=True)

        device = serializer.validated_data["device_id"]

        try:
            hub.pair_device(device)
        except DeviceAlreadyPairedError as e:
            return Response({"error": str(e)}, status=400)

        return Response({"status": "Device paired successfully"})

    @action(detail=True, methods=["get"], url_path="device-state/(?P<device_id>[^/.]+)")
    def get_device_state(self, request, pk: int, device_id: int):
        hub: Hub = self.get_object()

        try:
            state = hub.get_device_state(device_id)
        except Device.DoesNotExist:
            return Response({"error": "Device not found"}, status=404)

        return Response({"state": state})

    @action(detail=True, methods=["get"], url_path="devices")
    def list_devices(self, request, pk: int):
        hub: Hub = self.get_object()
        serializer = self.get_serializer(hub, action="list_devices")
        return Response(serializer.data)

    @action(
        detail=True, methods=["post"], url_path="remove-device/(?P<device_id>[^/.]+)"
    )
    def remove_device(self, request, pk: int, device_id: int):
        hub: Hub = self.get_object()

        try:
            hub.remove_device(device_id)
        except Device.DoesNotExist:
            return Response({"error": "Device not found"}, status=404)

        return Response({"status": "Device removed successfully"})


router.register(
    r"hubs",
    HubViewSet,
    basename="hubs",
)
