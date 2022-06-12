from django.contrib import admin

from .models import Color


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    shown_fields = ("id", "user", "color", "number")
    list_display = shown_fields
    list_editable = ("color", "number")
    list_display_links = ("id", "user")
    search_fields = shown_fields
    list_filter = shown_fields
