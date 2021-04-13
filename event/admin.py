from django.contrib import admin

from .models import Event, Option


class OptionInline(admin.TabularInline):
    model = Option
    readonly_fields = ("id", "created_at")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "created_at", "updated_at")
    inlines = (OptionInline,)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    readonly_fields,
                    "owner",
                    "title",
                    "description",
                    "timezone",
                    "optional",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "owner",
                    "title",
                    "description",
                    "timezone",
                    "optional",
                ),
            },
        ),
    )
    list_display = ("title", "owner", "timezone", "optional")
    ordering = ("title", "owner")
    search_fields = ("title", "description")
