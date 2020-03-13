# Generated by Django 2.2.10 on 2020-03-05 12:04

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("municipales", "0012_communepage_mandataire_email")]

    operations = [
        migrations.AlterField(
            model_name="communepage",
            name="code",
            field=models.CharField(
                editable=False, max_length=10, verbose_name="Code INSEE"
            ),
        ),
        migrations.CreateModel(
            name="Liste",
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
                    "code",
                    models.CharField(
                        editable=False, max_length=20, unique=True, verbose_name="Code"
                    ),
                ),
                (
                    "nom",
                    models.CharField(max_length=300, verbose_name="Nom de la liste"),
                ),
                (
                    "nuance",
                    models.CharField(
                        choices=[
                            ("LDVC", "Divers centre"),
                            ("LDVG", "Divers gauche"),
                            ("LEXG", "Extrême gauche"),
                            ("LDIV", "Divers"),
                            ("LDVD", "Divers droite"),
                            ("LREM", "LREM"),
                            ("LUG", "Union de la gauche"),
                            ("LUD", "Union de la droite"),
                            ("LRN", "Rassemblement national"),
                            ("LECO", "Autre Ecologiste"),
                            ("LSOC", "Socialiste"),
                            ("LCOM", "Communiste"),
                            ("LFI", "FI"),
                            ("LVEC", "EELV"),
                            ("LUDI", "UDI"),
                            ("LLR", "Les Républicains"),
                            ("LDLF", "Debout la France"),
                            ("LEXD", "Extrême droite"),
                            ("LRDG", "Parti radical de gauche"),
                            ("LMDM", "Modem"),
                            ("LUC", "Union du centre"),
                            ("LREG", "Régionaliste"),
                            ("LGJ", "Gilets Jaunes"),
                        ],
                        max_length=4,
                        verbose_name="Nuance politique",
                    ),
                ),
                (
                    "candidats",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=200),
                        size=None,
                        verbose_name="Candidats",
                    ),
                ),
                (
                    "soutien",
                    models.CharField(
                        choices=[
                            ("P", "Soutien et participation de la FI"),
                            ("O", "Préférence de la FI sans soutien"),
                            ("N", "Non soutenue"),
                        ],
                        default="N",
                        max_length=1,
                        verbose_name="Soutien ou participation de la FI",
                    ),
                ),
                (
                    "commune",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="municipales.CommunePage",
                    ),
                ),
            ],
        ),
    ]