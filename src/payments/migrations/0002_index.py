# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "CREATE INDEX systempay_id ON payments_payment (mod(id, 900000))",
            reverse_sql='drop index systempay_id;'
        )
    ]