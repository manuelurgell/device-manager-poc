from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from devices.models import Device


class Hub(models.Model):
    """A hardware piece that interacts with devices."""

    dwelling = models.ForeignKey(
        "dwellings.Dwelling",
        related_name="hubs",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    name = models.CharField(max_length=100, blank=True, null=True)

    def pair_device(self, device: "Device") -> None:
        """Pair a device to this hub."""
        device.pair_to_hub(self)

    def remove_device(self, device_id: int) -> None:
        """Remove a device from this hub."""
        device: "Device" = self.devices.get(id=device_id)
        device.unpair()

    def get_device_state(self, device_id: int) -> dict:
        """Get the state of a device by its ID."""
        device: "Device" = self.devices.get(id=device_id)
        return device.state
