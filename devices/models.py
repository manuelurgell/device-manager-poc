from typing import TYPE_CHECKING

from django.db import models

from devices.exceptions import DeviceAlreadyPairedError

if TYPE_CHECKING:
    from hubs.models import Hub


class Device(models.Model):
    """A smart device that can be controlled."""

    DEVICE_TYPES = [
        ("switch", "Switch"),
        ("dimmer", "Dimmer"),
        ("lock", "Lock"),
        ("thermostat", "Thermostat"),
    ]

    hub = models.ForeignKey(
        "hubs.Hub",
        related_name="devices",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    state = models.JSONField(default=dict)
    paired = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        """Override delete to prevent deletion of paired devices."""
        if self.paired:
            raise DeviceAlreadyPairedError("Cannot delete a paired device")
        super().delete(*args, **kwargs)

    def pair_to_hub(self, hub: "Hub"):
        """Pair this device to a hub."""
        if self.paired:
            raise DeviceAlreadyPairedError("Device already paired")

        self.hub = hub
        self.paired = True
        self.save()

    def unpair(self):
        """Unpair this device from its hub."""
        self.hub = None
        self.paired = False
        self.save()
