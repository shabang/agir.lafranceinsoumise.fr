# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 17:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, help_text="UUID interne à l'API pour identifier la ressource", primary_key=True, serialize=False, verbose_name='UUID')),
                ('nb_id', models.IntegerField(help_text="L'identifiant de la ressource correspondante sur NationBuilder, si importé.", null=True, unique=True, verbose_name='ID sur NationBuilder')),
                ('coordinates_lat', models.DecimalField(decimal_places=6, max_digits=9, null=True, verbose_name='latitude géographique')),
                ('coordinates_lon', models.DecimalField(decimal_places=6, max_digits=9, null=True, verbose_name='longitude géographique')),
                ('location_name', models.CharField(blank=True, max_length=255, verbose_name='nom du lieu')),
                ('location_address', models.CharField(blank=True, max_length=255, verbose_name='adresse complète')),
                ('location_address1', models.CharField(blank=True, max_length=100, verbose_name='adresse (1ère ligne)')),
                ('location_address2', models.CharField(blank=True, max_length=100, verbose_name='adresse (2ème ligne)')),
                ('location_city', models.CharField(blank=True, max_length=100, verbose_name='ville')),
                ('location_zip', models.CharField(blank=True, max_length=20, verbose_name='code postal')),
                ('location_state', models.CharField(blank=True, max_length=40, verbose_name='état')),
                ('location_country', django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='pays')),
                ('email', models.EmailField(help_text="L'adresse email de la personne, utilisée comme identifiant", max_length=254, unique=True, verbose_name='adresse email')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='prénom')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='nom de famille')),
                ('bounced', models.BooleanField(default=False, help_text='Indique que des mails envoyés ont été rejetés par le serveur distant', verbose_name='email rejeté')),
                ('bounced_date', models.DateTimeField(help_text='Si des mails ont été rejetés, indique la date du dernier rejet', null=True, verbose_name="date de rejet de l'email")),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'personne',
                'verbose_name_plural': 'personnes',
                'ordering': ('email',),
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='PersonTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30, unique=True, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'tag',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='people', to='people.PersonTag'),
        ),
    ]
