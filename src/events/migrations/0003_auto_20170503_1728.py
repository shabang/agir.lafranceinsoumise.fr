# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_add_initial_relations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='events', through='events.RSVP', to='people.Person'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(related_name='organized_events', to='people.Person'),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvps', to='people.Person'),
        ),
    ]
