# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_polls'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='La consultation sera automatiquement fermée à ce moment', verbose_name='Date et heure de fin de la consultation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='La consultation sera automatiquement ouverte à ce moment', verbose_name='Date et heure de début de la consultation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.TextField(help_text='Le texte de description affiché pour tous les insoumis', verbose_name='Description de la consultation'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titre de la consultation'),
        ),
        migrations.AlterField(
            model_name='polloption',
            name='description',
            field=models.TextField(help_text="Option telle qu'elle apparaîtra aux insoumis⋅es.", verbose_name='Option'),
        ),
        migrations.AlterField(
            model_name='polloption',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='polls.Poll'),
        ),
    ]