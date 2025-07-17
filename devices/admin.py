from django.contrib import admin

from devices.models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """Admin interface for Device model."""

    list_display = ("id", "type", "paired", "hub")
    search_fields = ("id", "type")
    list_filter = ("type", "paired", "hub")
