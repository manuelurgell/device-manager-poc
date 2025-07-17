from rest_framework.response import Response

from app.urls import router
from devices import serializers
from devices.exceptions import DeviceAlreadyPairedError
from devices.models import Device
from utils.mixins import (
    BaseGenericViewSet,
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


class DeviceViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    BaseGenericViewSet,
):

    queryset = Device.objects.all()

    list_serializer_class = serializers.DeviceSerializer
    create_serializer_class = serializers.DeviceCreateSerializer
    retrieve_serializer_class = serializers.DeviceStateSerializer
    update_serializer_class = serializers.DeviceStateSerializer
    destroy_serializer_class = serializers.DeviceSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except DeviceAlreadyPairedError as e:
            return Response({"error": str(e)}, status=400)


router.register(
    r"devices",
    DeviceViewSet,
    basename="devices",
)
