# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


def copy_calendar_information(apps, schema):
    Event = apps.get_model("events", "Event")
    CalendarItem = apps.get_model("events", "CalendarItem")

    CalendarItem.objects.bulk_create(
        [
            CalendarItem(event=e, calendar_id=e.calendar_id)
            for e in Event.objects.iterator()
        ]
    )


class Migration(migrations.Migration):

    dependencies = [("events", "0036_auto_20180220_1842")]

    operations = [
        migrations.CreateModel(
            name="CalendarItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "calendar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="events.Calendar",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="calendaritem",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="calendar_items",
                to="events.Event",
            ),
        ),
        migrations.RunPython(copy_calendar_information, migrations.RunPython.noop),
        migrations.RemoveField(model_name="event", name="calendar"),
        migrations.AddField(
            model_name="calendar",
            name="events",
            field=models.ManyToManyField(
                related_name="calendars",
                through="events.CalendarItem",
                to="events.Event",
            ),
        ),
    ]
