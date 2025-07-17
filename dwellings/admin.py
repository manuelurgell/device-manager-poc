from django.contrib import admin

from dwellings.models import Dwelling


@admin.register(Dwelling)
class DwellingAdmin(admin.ModelAdmin):
    """Admin interface for Dwelling model."""

    list_display = ("id", "occupied")
    search_fields = ("id",)
