# Generated by Django 2.2.14 on 2020-07-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elus", "0011_auto_20200723_1616"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mandatdepartemental",
            name="mandat",
            field=models.CharField(
                choices=[
                    ("INC", "Situation au conseil inconnue"),
                    ("MAJ", "Conseiller⋅e majoritaire"),
                    ("OPP", "Conseiller⋅e minoritaire"),
                    ("PRE", "Président"),
                    ("VPR", "Vice-Président"),
                ],
                default="INC",
                max_length=3,
                verbose_name="Type de mandat",
            ),
        ),
        migrations.AlterField(
            model_name="mandatregional",
            name="mandat",
            field=models.CharField(
                choices=[
                    ("INC", "Situation au conseil inconnue"),
                    ("MAJ", "Conseiller⋅e majoritaire"),
                    ("OPP", "Conseiller⋅e minoritaire"),
                    ("PRE", "Président"),
                    ("VPR", "Vice-Président"),
                ],
                default="INC",
                max_length=3,
                verbose_name="Type de mandat",
            ),
        ),
    ]