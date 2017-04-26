from django.db import models, transaction
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from model_utils.models import TimeStampedModel

from lib.models import BaseAPIResource, AbstractLabel, RoleProxy
from authentication.models import Role


class ClientManager(models.Manager):
    def get_by_natural_key(self, label):
        return self.select_related('role').get(label=label)

    def _create_client(self, label, password, *, is_superuser, is_active=True, **extra_fields):
        """
        Creates and saves a client with the given label and password.
        """
        if not label:
            raise ValueError('Label must be set')

        role = Role(type=Role.CLIENT_ROLE, is_superuser=is_superuser, is_active=is_active)
        role.set_password(password)

        with transaction.atomic():
            role.save()
            client = self.model(label=label, role=role, **extra_fields)
            client.save(using=self._db)

        return client

    def create_client(self, label, password=None, **extra_fields):
        """
        Create a client 
        :param label: the user's email
        :param password: optional password that may be used to connect to the API
        :param extra_fields: any other field
        :return: 
        """
        extra_fields.setdefault('is_superuser', False)
        return self._create_client(label, password, **extra_fields)

    def create_superclient(self, label, password, **extra_fields):
        """
        Create a super client
        :param label: 
        :param password: 
        :param extra_fields: 
        :return: 
        """
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_client(label, password, **extra_fields)


class Client(RoleProxy, BaseAPIResource):
    objects = ClientManager()

    role = models.OneToOneField('authentication.Role', on_delete=models.PROTECT, related_name='client', null=False)

    label = models.CharField(
        _('identifiant du client'),
        max_length=40,
        blank=False,
        unique=True,
        help_text=_("L'identifiant du client, utilisé pour l'authentication.")
    )

    name = models.CharField(
        _('nom du client'),
        max_length=150,
        blank=False,
        help_text=_("Le nom du client, tel qu'affiché à l'utilisateur lorsqu'il autorise ce client.")
    )

    description = models.TextField(
        _('description du client'),
        blank=True,
        help_text=_("Une description du client à l'intention des utilisateurs éventuels.")
    )

    trusted = models.BooleanField(
        _('client de confiance'),
        default=False,
        help_text=_("Indique si ce client est de confiance : s'il l'est, l'utilisateur n'a pas besoin de "
                    "valider l'autorisation lors de la procédure OAuth.")
    )

    uris = ArrayField(
        models.CharField(max_length=150, blank=False),
        verbose_name=_('URIs de redirection OAuth'),
        default=list,
        size=4,
        help_text=_("La liste des URIs auxquelles le serveur d'authentification acceptera de rediriger les "
                    "utilisateurs pendant la procédure OAuth.")
    )

    scopes = models.ManyToManyField(
        'Scope',
        related_name='clients',
        blank=True,
        help_text=_('La liste des scopes autorisés pour ce client.')
    )

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ('label',)
        default_permissions = ('add', 'change', 'delete', 'view')


class Scope(AbstractLabel):
    class Meta:
        verbose_name = _('scope')
        verbose_name_plural = _('scopes')


class Authorization(TimeStampedModel):
    person = models.ForeignKey('people.Person', related_name='authorizations')
    client = models.ForeignKey('Client', related_name='authorizations')
    scopes = models.ManyToManyField('Scope', related_name='authorizations')

    class Meta:
        verbose_name = 'autorisation',
        verbose_name_plural = 'autorisations'
        unique_together = ('person', 'client')
