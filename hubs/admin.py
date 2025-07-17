from django.contrib import admin

from hubs.models import Hub


@admin.register(Hub)
class HubAdmin(admin.ModelAdmin):
    """Admin interface for Hub model."""

    list_display = ("id", "dwelling")
    search_fields = ("id",)
    list_filter = ("dwelling",)
