# Generated by Django 2.2.14 on 2020-07-01 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0062_auto_20200330_1252"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="created",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="date de création",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name="dernière modification"
            ),
        ),
        migrations.AlterField(
            model_name="personform",
            name="created",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="date de création",
            ),
        ),
        migrations.AlterField(
            model_name="personform",
            name="modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name="dernière modification"
            ),
        ),
        migrations.AlterField(
            model_name="personformsubmission",
            name="created",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="date de création",
            ),
        ),
        migrations.AlterField(
            model_name="personformsubmission",
            name="modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name="dernière modification"
            ),
        ),
        migrations.AlterField(
            model_name="personvalidationsms",
            name="created",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="date de création",
            ),
        ),
        migrations.AlterField(
            model_name="personvalidationsms",
            name="modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name="dernière modification"
            ),
        ),
    ]