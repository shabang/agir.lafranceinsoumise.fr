import uuid
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class RoleManager(BaseUserManager):
    pass


class Role(PermissionsMixin, AbstractBaseUser):
    PERSON_ROLE = 'P'
    CLIENT_ROLE = 'C'

    ROLE_TYPE = [
        (PERSON_ROLE, _('Personne')),
        (CLIENT_ROLE, _('Client'))
    ]

    objects = RoleManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(_('type de rôle'), max_length=1, choices=ROLE_TYPE, editable=False, blank=False, null=False)

    USERNAME_FIELD = 'id'

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
