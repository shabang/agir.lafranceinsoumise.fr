# Generated by Django 2.1.7 on 2019-03-13 17:42

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [("people", "0051_personform_config")]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="location_country",
            field=django_countries.fields.CountryField(
                blank=True, default="FR", max_length=2, verbose_name="pays"
            ),
        ),
        migrations.AlterField(
            model_name="personform",
            name="config",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=dict, verbose_name="Configuration"
            ),
        ),
    ]
