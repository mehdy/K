from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from K.models import Model


class Event(Model):
    title = models.CharField(_("title"), max_length=64, blank=False, null=False)
    description = models.CharField(_("description"), max_length=4096, blank=True)
    timezone = models.CharField(_("timezone"), max_length=32, blank=False, null=False, default="UTC")
    optional = models.BooleanField(_("optional"), default=False)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="events", on_delete=models.CASCADE)


class Option(Model):
    start_at = models.DateTimeField(_("start at"), blank=False, null=False)
    finish_at = models.DateTimeField(_("finish at"), blank=False, null=False)

    event = models.ForeignKey(Event, related_name="options", on_delete=models.CASCADE)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="votes")
