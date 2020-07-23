# Generated by Django 2.2.14 on 2020-07-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elus", "0008_plusieurs_mandats"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mandatdepartemental",
            name="statut",
            field=models.CharField(
                choices=[
                    ("INC", "Mandat à vérifier (ajouté côté admin)"),
                    ("DEM", "Mandat à vérifier (ajouté par la personne elle-même)"),
                    ("IMP", "Importé par une opération automatique"),
                    ("INS", "Mandat vérifié"),
                ],
                default="INC",
                max_length=3,
                verbose_name="Statut",
            ),
        ),
        migrations.AlterField(
            model_name="mandatmunicipal",
            name="communautaire",
            field=models.CharField(
                choices=[
                    ("NON", "Pas de mandat communautaire"),
                    ("INC", "Délégué⋅e, situation inconnue"),
                    ("MAJ", "Délégué⋅e majoritaire"),
                    ("OPP", "Délégué⋅e minoritaire"),
                    ("PRE", "Président"),
                    ("VPR", "Vice-Président"),
                ],
                default="NON",
                max_length=3,
                verbose_name="Élu EPCI",
            ),
        ),
        migrations.AlterField(
            model_name="mandatmunicipal",
            name="statut",
            field=models.CharField(
                choices=[
                    ("INC", "Mandat à vérifier (ajouté côté admin)"),
                    ("DEM", "Mandat à vérifier (ajouté par la personne elle-même)"),
                    ("IMP", "Importé par une opération automatique"),
                    ("INS", "Mandat vérifié"),
                ],
                default="INC",
                max_length=3,
                verbose_name="Statut",
            ),
        ),
        migrations.AlterField(
            model_name="mandatregional",
            name="statut",
            field=models.CharField(
                choices=[
                    ("INC", "Mandat à vérifier (ajouté côté admin)"),
                    ("DEM", "Mandat à vérifier (ajouté par la personne elle-même)"),
                    ("IMP", "Importé par une opération automatique"),
                    ("INS", "Mandat vérifié"),
                ],
                default="INC",
                max_length=3,
                verbose_name="Statut",
            ),
        ),
    ]