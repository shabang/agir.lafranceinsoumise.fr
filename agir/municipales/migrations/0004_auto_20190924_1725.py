# Generated by Django 2.2.5 on 2019-09-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("municipales", "0003_auto_20190913_1507")]

    operations = [
        migrations.AddField(
            model_name="communepage",
            name="facebook",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Identifiant Facebook"
            ),
        ),
        migrations.AddField(
            model_name="communepage",
            name="first_name_1",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Prénom chef⋅fe de file 1"
            ),
        ),
        migrations.AddField(
            model_name="communepage",
            name="first_name_2",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Prénom chef⋅fe de file 2"
            ),
        ),
        migrations.AddField(
            model_name="communepage",
            name="last_name_1",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Nom chef⋅fe de file 1"
            ),
        ),
        migrations.AddField(
            model_name="communepage",
            name="last_name_2",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Nom chef⋅fe de file 2"
            ),
        ),
        migrations.AddField(
            model_name="communepage",
            name="municipale_list_name",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Nom de la liste"
            ),
        ),
        migrations.AddField(
            model_name="communepage",
            name="website",
            field=models.URLField(blank=True, max_length=255, verbose_name="Site web"),
        ),
    ]
