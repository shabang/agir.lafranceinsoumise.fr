# Generated by Django 2.2.14 on 2020-07-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0063_auto_20200701_1622"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="membre_reseau_elus",
            field=models.CharField(
                default="I",
                help_text="Pertinent uniquement si la personne a un ou plusieurs mandats électoraux.",
                max_length=1,
                verbose_name="Membre du réseau des élus",
            ),
        ),
    ]
