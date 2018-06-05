# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-26 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_supportgroup_contact_hide_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='notifications_enabled',
            field=models.BooleanField(default=True, help_text='Je recevrai des messages en cas de modification du groupe.', verbose_name='Recevoir les notifications de ce groupe'),
        ),
    ]