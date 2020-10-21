# Generated by Django 3.1.2 on 2020-10-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0031_elus"),
    ]

    operations = [
        migrations.AlterField(
            model_name="segment",
            name="draw_status",
            field=models.BooleanField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Limiter aux gens dont l'inscription au tirage au sort est",
            ),
        ),
    ]
