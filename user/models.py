from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from K.models import Model


class User(Model, AbstractUser):
    # Disable date_joined as we have created_at
    date_joined = None

    first_name = models.CharField(_("first name"), max_length=32, blank=True)
    last_name = models.CharField(_("last name"), max_length=32, blank=True)
    username = models.CharField(
        _("username"),
        max_length=32,
        unique=True,
        db_index=True,
        blank=False,
        validators=[
            MinLengthValidator(3),
            RegexValidator(
                regex=r"^[\w_]*$",
                message=_("Username may contain only letters, numbers and underscore characters."),
            ),
        ],
    )
    email = models.EmailField(
        _("email address"),
        max_length=64,
        unique=True,
        db_index=True,
        blank=False,
        validators=[MinLengthValidator(6)],
    )
