from django.contrib import messages
from django.core.exceptions import ValidationError
from django.urls import reverse

from agir.authentication.backend_mixins import GetRoleMixin
from agir.authentication.tokens import connection_token_generator, short_code_generator
from agir.people.models import Person


class ShortCodeBackend(GetRoleMixin):
    prefetch = ["person"]

    def authenticate(self, request, user_pk=None, short_code=None):
        if user_pk and short_code:
            login_meta = short_code_generator.check_short_code(user_pk, short_code)
            if login_meta is not None:
                try:
                    person = Person.objects.select_related("role").get(pk=user_pk)
                    person.ensure_role_exists()
                    role = person.role
                except (Person.DoesNotExist, ValidationError):
                    return None

                if self.user_can_authenticate(role):
                    role.login_meta = (
                        login_meta  # on annote le role avec les metas de connexion
                    )
                    return role

        return None


class MailLinkBackend(GetRoleMixin):
    prefetch = ["person"]

    def authenticate(self, request, user_pk=None, token=None):
        if user_pk and token:
            try:
                person = Person.objects.select_related("role").get(pk=user_pk)
            except (Person.DoesNotExist, ValidationError):
                return None
            if connection_token_generator.check_token(token, user=person):
                person.ensure_role_exists()
                if self.user_can_authenticate(person.role):
                    return person.role

        return None
