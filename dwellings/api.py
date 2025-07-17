from rest_framework.decorators import action
from rest_framework.response import Response

from app.urls import router
from dwellings import serializers
from dwellings.models import Dwelling
from utils.mixins import BaseGenericViewSet, CreateModelMixin, ListModelMixin


class DwellingViewSet(
    ListModelMixin,
    CreateModelMixin,
    BaseGenericViewSet,
):

    queryset = Dwelling.objects.all()

    list_serializer_class = serializers.DwellingSerializer
    create_serializer_class = serializers.DwellingCreateSerializer

    install_hub_serializer_class = serializers.DwellingInstallHubSerializer

    @action(detail=True, methods=["post"], url_path="set-occupied")
    def set_occupied(self, request, pk: int):
        dwelling: Dwelling = self.get_object()
        dwelling.set_occupied()
        return Response({"status": "Dwelling set to occupied"})

    @action(detail=True, methods=["post"], url_path="set-vacant")
    def set_vacant(self, request, pk: int):
        dwelling: Dwelling = self.get_object()
        dwelling.set_vacant()
        return Response({"status": "Dwelling set to vacant"})

    @action(detail=True, methods=["post"], url_path="install-hub")
    def install_hub(self, request, pk: int):
        dwelling: Dwelling = self.get_object()

        serializer = self.get_serializer(data=request.data, action="install_hub")
        serializer.is_valid(raise_exception=True)

        hub = serializer.validated_data["hub_id"]
        dwelling.install_hub(hub)

        return Response({"status": "Hub installed successfully"})


router.register(
    r"dwellings",
    DwellingViewSet,
    basename="dwellings",
)
