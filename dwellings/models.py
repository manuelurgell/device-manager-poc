from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from hubs.models import Hub


class Dwelling(models.Model):
    """A living space where hubs and devices can be installed."""

    name = models.CharField(max_length=100, blank=True, null=True)
    occupied = models.BooleanField(default=False)

    def set_occupied(self):
        self.occupied = True
        self.save()

    def set_vacant(self):
        self.occupied = False
        self.save()

    def install_hub(self, hub: "Hub"):
        hub.dwelling = self
        hub.save()
